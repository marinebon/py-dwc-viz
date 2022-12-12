"""
taxon: visualize taxonomic distributions
"""
try:
    import plotly.express as px
except:
    print("This module uses plotly to plot a sunburst plot of taxonomic distribution. We could not find a version of plotly on your system.")
import matplotlib.pyplot as plt
import pandas as pd

def plot_dist(data, **kwargs):
    """
    Generates a plotly sunburst plot from a DataFrame of occurrence records.

    :param data: [Pandas DataFrame] A Pandas DataFrame of occurrence records with 
        columns ["kingdom", "phylum", "class", "order", "family", "genus","species"].

    :return: A plotly sunburst plot figure object

    Usage::

        from pydwcviz import taxon
        from pyobis import occurrences

        # get the data
        fig = taxon.plot_dist(occurrences.search(scientificname = "Mola mola").execute())
        
        # show the figure
        fig.show()
    """

    fig = px.sunburst(
        data.fillna(
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

def latdist(data, level="Species", bbox_to_anchor = [1.5, 1.2], interactive=False):
    """
    Generates a line plot of taxonomic distribution against latitude at a taxonomic level
    
    :param data: [Pandas DataFrame]  A Pandas DataFrame of occurrence records with 
        columns ["kingdom", "phylum", "class", "order", "family", "genus","species"].
    :param level: [String] Taxonomic level to plot distribution at. One of 
        ["kingdom", "phylum", "class", "order", "family", "genus","species"].
    :param bbox_to_anchor: [List <Float>] Position to anchor bounding box for easy viewing of legend.
    :param interactive: [Boolean] If True, the matplotlib plot. If False then plotly interactive plot
    :return: A Matplotlib axes object.

    Usage::

        from pydwcviz import taxon
        from pyobis import occurrences

        # plot the figure with the data
        taxon.latdist(occurrences.search(scientificname = "Mola mola").execute(), level="species", interactive=False)

        # interactive plot using plotly
        fig = taxon.latdist(occurrences.search(scientificname = "Mola mola").execute(), level="species", interactive=True)
        fig.show()
    """
    # groupby a certain level
    l = data.groupby([level, "decimalLatitude"]).scientificName.count()
    df = pd.DataFrame(l)
    df.loc[:,[level, "lat"]] = l.index.tolist()
    df.rename(columns = {'scientificName':'count'}, inplace=True)

    df.sort_values("lat", inplace=True)
    
    if not interactive:
        fig, ax = plt.subplots(1,1,sharex=True,sharey=True)
        for i in df[level].unique():
            df[df[level]==i].plot(x = "count", y="lat", label=i, ax = ax)
        
        plt.ylabel("latitude")
        plt.title("Latitude v/s Occurrence Counts")
        plt.legend(bbox_to_anchor=bbox_to_anchor)

        return ax
    else:
        fig = px.line(df, x = "count",y ="lat", color=level)
        fig.update_layout(title="Latitude v/s Occurrence Counts")
        return fig
