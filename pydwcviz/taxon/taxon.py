"""
taxon: visualize taxonomic distributions
"""
try:
    import plotly.express as px
except:
    print("This module uses plotly to plot a sunburst plot of taxonomic distribution. We could not find a version of plotly on your system.")
import matplotlib.pyplot as plt
import pandas as pd

def plot_dist(df, **kwargs):
    """
    Generates a plotly sunburst plot from a DataFrame of occurrence records.

    :param df: [Pandas DataFrame] A Pandas DataFrame of occurrence records with 
        columns ["kingdom", "phylum", "class", "order", "family", "genus","species"].

    :return: A plotly sunburst plot figure object

    Usage::

        from pydwcviz import taxon
        from pyobis.occurrences import OccQuery
        occ = OccQuery()

        # get the data
        fig = taxon.plot_dist(occ.search(scientificname = "Mola mola"))
        
        # show the figure
        fig.show()
    """

    fig = px.sunburst(
        df.fillna(
            {'phylum':'None',
            'order':"None",
            'class':"None",
            'family':"None",
            'genus':"None",
            'species':"None"
            }),
        path=["kingdom", "phylum", "class", "order", "family", "genus","species"],
        width=750, height=750,
        title="Taxonomic Distribution",
    )
    fig.update_traces(textinfo="label+percent parent")
    return fig

def latdist(data, level="Species"):
    """
    Generates a line plot of taxonomic distribution against latitude at a taxonomic level
    
    :param df: [Pandas DataFrame]  A Pandas DataFrame of occurrence records with 
        columns ["kingdom", "phylum", "class", "order", "family", "genus","species"].
    :param level: [String] Taxonomic level to plot distribution at. One of 
        ["kingdom", "phylum", "class", "order", "family", "genus","species"].

    :return: A Matplotlib axes object.

    Usage::

        from pydwcviz import taxon
        from pyobis import occurrences

        # get the data
        fig = taxon.latdist(occurrences.search(scientificname = "Mola mola"), level="species")
        
        # show the figure
        fig.show()
    """
    # groupby a certain level
    l = data.groupby([level, "decimalLatitude"]).scientificName.count()
    df = pd.DataFrame(l)
    df.loc[:,["taxa", "lat"]] = l.index.tolist()
    df.index = range(len(df))

    df.sort_values("lat", inplace=True)
    print("dit")
    fig, ax = plt.subplots(1,1,sharex=True,sharey=True)
    for i in df["taxa"].unique():
        df[df["taxa"]==i].plot(x = "scientificName", y="lat", label=i, ax = ax)
    
    plt.xlabel("count")
    plt.ylabel("latitude")
    plt.title("Latitude v/s Occurrence Counts")
    plt.legend(bbox_to_anchor=[1.3, 0.8])

    return plt.show()