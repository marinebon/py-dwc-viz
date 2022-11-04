"""
taxon: visualize taxonomic distributions
"""
try:
    import plotly.express as px
except:
    print("This module uses plotly to plot a sunburst plot of taxonomic distribution. We could not find a version of plotly on your system.")

def plot_dist(df, **kwargs):
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
    return fig.show()