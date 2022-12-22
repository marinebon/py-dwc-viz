"""
diversity: generate biodiversity indices for species analysis.
"""
import pandas as pd
import math

def shannon(df, decimals=3):
    """
    Generate Shannon's Diversity Index from species occurrence data.

    :param df: [DataFrame] DataFrame. Species Occurrence data as a pandas DataFrame
    :param decimals: [Integer] Decimals. Precision to be maintained in coordinates. 
        Used for aggregation of records (binning).

    :: Usage

        from pyobis import occurrences
        from pydwcviz import diversity

        data = occurrences.search(
            # this is a geometry in the Arabian Sea (right of India)
            geometry="POLYGON ((58.3301 19.0935, 69.8145 19.0381, 69.8145 9.5161, 58.6230 9.6316, 58.3301 19.0935))", 
        ).execute()
        
        diversity.shannon(data, 3)
    """
    if "id" not in df.columns:
        df.rename({"gbifID":"id"}, inplace=True)
    
    
    _df = df.dropna(subset=["species"])
        .round(
            {"decimalLongitude":decimals, "decimalLatitude":decimals}
        )[["decimalLongitude","decimalLatitude","species","id"]]
    print(f"{len(df.index) - len(_df.index)} NA-containing records dropped.")
    
    _sh_df = pd.DataFrame(
        _df.groupby(["decimalLongitude", "decimalLatitude", "species"]).id.count()
    )
    print(f"{len(_sh_df.index)} unique species*locations found.")
    
    # calculate the index
    _sh_df["sum"] = _df.groupby(["decimalLongitude", "decimalLatitude"]).id.count()
    _sh_df["coeff"] = _sh_df["id"] / _sh_df["sum"] * (_sh_df["id"] / _sh_df["sum"]).apply(math.log)
    
    return _sh_df.reset_index().groupby(["decimalLongitude", "decimalLatitude"]).coeff.sum().reset_index()
