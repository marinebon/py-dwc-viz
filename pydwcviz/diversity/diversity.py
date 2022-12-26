"""
diversity: generate biodiversity indices for species analysis.
"""
import pandas as pd
import numpy as np
from scipy.special import loggamma
import math

def shannon(df, decimals=3):
    """
    Generate Shannon's Diversity Index from species occurrence data.

    :param df: [DataFrame] DataFrame. Species Occurrence data as a pandas DataFrame
    :param decimals: [Integer] Decimals. Precision to be maintained in coordinates. 
        Used for aggregation of records (binning).

    :return: A DataFrame

    Usage::

        from pyobis import occurrences
        from pydwcviz import diversity

        data = occurrences.search(
            # this is a geometry in the Arabian Sea (right of India)
            geometry="POLYGON ((58.3301 19.0935, 69.8145 19.0381, 69.8145 9.5161, 58.6230 9.6316, 58.3301 19.0935))", 
        ).execute()
        
        diversity.shannon(data, 3)
    """
    # if the data source is GBIF then convert it to compatible format (column headings)
    if "id" not in df.columns:
        df.rename({"gbifID":"id"}, inplace=True)
    
    # prepare index only for species and drop unnecessary columns
    _df = df.dropna(subset=["species"]).round(
        {"decimalLongitude":decimals, "decimalLatitude":decimals}
        )[["decimalLongitude","decimalLatitude","species","id"]]
    print(f"{len(df.index) - len(_df.index)} Not species records dropped.")
    
    # aggregate number of records as a proxy for estimating abundance
    _sh_df = pd.DataFrame(
        _df.groupby(["decimalLongitude", "decimalLatitude", "species"]).id.count()
    )
    print(f"{len(_sh_df.index)} unique species*locations records found.")
    
    # preparing the Pi for each species*location pair and calculating individual coefficients
    _sh_df["sum"] = _df.groupby(["decimalLongitude", "decimalLatitude"]).id.count()
    _sh_df["coeff"] = _sh_df["id"] / _sh_df["sum"] * (_sh_df["id"] / _sh_df["sum"]).apply(math.log)
    
    # sum up coefficients for all species in a location and calculate the total biodiversity
    return _sh_df.reset_index().groupby(["decimalLongitude", "decimalLatitude"]).coeff.sum().reset_index()

def es50(df, decimals=3):
    """
    Generate ES50 (Hulbert's) Diversity Index from species occurrence data.

    :param df: [DataFrame] DataFrame. Species Occurrence data as a pandas DataFrame with at least ['decimalLongitude','decimalLatitude', 'id', 'species']
    :param decimals: [Integer] Decimals. Precision to be maintained in coordinates. Used for aggregation of records (binning).

    :return: A DataFrame
    
    Usage::

        from pyobis import occurrences
        from pydwcviz import diversity

        data = occurrences.search(
            # this is a geometry in the Arabian Sea (right of India)
            geometry="POLYGON ((58.3301 19.0935, 69.8145 19.0381, 69.8145 9.5161, 58.6230 9.6316, 58.3301 19.0935))", 
        ).execute()
        
        diversity.es50(data, 3)
    """
    # pick only the required columns and drop non-species records
    df = df.dropna(subset=["species"])[["decimalLongitude","decimalLatitude","species","id"]].round({"decimalLongitude":decimals,"decimalLatitude":decimals})

    # calculate n-ni for all species*locations pair
    es_df = pd.DataFrame(
        df.groupby(["decimalLongitude","decimalLatitude"]).id.count() - df.groupby(["decimalLongitude","decimalLatitude","species"]).id.count()
        ).rename(columns={'id':'n-ni'})

    # calculate the n for each location
    es_df["n"] = df.groupby(["decimalLongitude","decimalLatitude"]).id.count()

    # calculate esi when n-ni>=50
    es_df["esi"] = 1 - np.exp((es_df[es_df["n-ni"]>=50]["n-ni"]+1).apply(loggamma) + (es_df[es_df["n-ni"]>=50]['n']-50+1).apply(loggamma) - (es_df[es_df["n-ni"]>=50]["n-ni"]-50+1).apply(loggamma) - (es_df[es_df["n-ni"]>=50]['n']+1).apply(loggamma))

    # calculate esi when n = 50
    es_df.loc[es_df["n"]==50, "esi"] = 1

    # calculate the sum for esi of all species in all locations to prepare a final table
    return pd.DataFrame(es_df.reset_index().groupby(["decimalLongitude","decimalLatitude"]).esi.sum()).reset_index()