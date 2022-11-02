import gif
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from pyobis import occurrences as occ

class Species:
  def __init__(self, name):
    """ 
    To plot species year-on-year on world map
    ::param species: [string] scientificname of species
    # Example Usage:
    # Plotting world map for a particular species
    wmap = species("Mola mola")
    wmap.plot()
    """
    self.name = name
    self.res = occ.search(scientificname=self.name)["results"]
    
    # dressing data i.e. cleans and removes NaNs
    df = pd.DataFrame(self.res)
    data = df[df["eventDate"].notna()]
    data = data[data["eventDate"].notnull()]
    data = data[data["eventDate"]!="#VALUE!"]
    data = data[data["eventDate"]!=np.NaN]
    data = data.replace('NA','0000-00-00')
    data = data[data["eventDate"]!='0000-00-00']
    data = data.sort_values(by="eventDate")
    data.eventDate = data.eventDate.str[:4].astype(int)
    
    # setting data object of the class to the cleaned data
    self.data=data

  def inter_plot(self):
    """
    Plot an interactive map using Plotly GeoObjects

    ::returns: an interactive IPython object that contains a plotly geomap
    """
    @interact
    def select_country(year = list(self.data.eventDate.unique())):
        fig = px.scatter_geo(self.data[self.data["eventDate"]==year],lat="decimalLatitude", lon="decimalLongitude", hover_name="scientificName")
        fig.update_layout(height=400, margin={"r":0,"t":40,"l":0,"b":10}, title=f"World map {self.data.scientificName[0]} in {year}")
        fig.show();

  def make_gif(self, year=None, duration=15):
    """
    To create a GIF of migration patterns after a threshold year (if provided else the starting year from records)
    ::param year: [Int] the threshold year. Plot all records on map only which are after this year. Default the starting year of records

    ::returns: a GIF. Saved at maps.gif
    """
    year =  year if year else self.res["eventDate"].min()
    _df = self.data[self.data["eventDate"]>=year]
    frames = []
    countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    # iterating over years and creating images
    @gif.frame
    def plotframes(year):
      sns.set(rc={'figure.figsize':(10,7)})
      countries.plot(color="lightgrey")
      p = sns.scatterplot(data=_df[_df["eventDate"]==year], x="decimalLongitude", y="decimalLatitude")
      p.set_title(f"{_df.scientificName[0]} - {year}");
    
    # plot maps
    for year in _df.eventDate.unique():
      frames.append(plotframes(year))
    gif.save(frames, "maps.gif", duration=duration, unit="s", between="startend")
    Image(open("maps.gif","rb").read())
