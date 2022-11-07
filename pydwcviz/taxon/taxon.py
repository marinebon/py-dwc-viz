"""
taxon: visualize taxonomic distributions
"""
try:
    import plotly.express as px
except:
    print("This module uses plotly to plot a sunburst plot of taxonomic distribution. We could not find a version of plotly on your system.")

def plot_dist(df, **kwargs):
    """
    Generates a plotly sunburst plot from a DataFrame of occurrence records.

    :param dataframe: [Pandas DataFrame] A Pandas DataFrame of occurrence records with 
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