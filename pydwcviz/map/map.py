"""
maps: visualize DwC data easily on maps
"""
import matplotlib.pyplot as plt
import geopandas as gpd

def points(df, crs="epsg:4326", figsize=(20,10)):
    """
    Generate a point map from DwC data

    :param df: [DataFrame] A DwC data DataFrame with at least decimalLongitude, and decimalLatitude
    as column labels
    :param crs: [String] Define the CRS for the map
    :param figsize: [Tuple] Define the figsize of the plot

    :return: A Matplotlib Axes Object

    Usage::

        from pyobis import occurrences
        from pydwcviz import map

        ax = map.points(occurrences.search(scientificname = "Mola mola").execute())
        plt.show()
    """
    gdf = gpd.GeoDataFrame(
        df, 
        geometry=gpd.points_from_xy(df.decimalLongitude, df.decimalLatitude),
        crs = crs,
    )

    fig, ax = plt.subplots(figsize=figsize)

    gdf.plot(ax=ax, markersize=5, zorder=10, legend=True)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world = world.to_crs(gdf.crs)
    world.plot(ax=ax, color='lightgrey', edgecolor='white', zorder=1)

    ax.set_axis_off()

    return ax