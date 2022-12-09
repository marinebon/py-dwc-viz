"""
Tests for taxon module
"""

from pydwcviz import taxon
from pyobis import occurrences

def test_plot_dist():
    """Test latitude distriution function - both interactive and non-interactive"""
    fig = taxon.plot_dist(occurrences.search(scientificname = "Mola mola", size=100).execute())
    assert fig.__class__.__name__ == "Figure"

def test_latdist():
    """Test latitude distriution function - both interactive and non-interactive"""
    assert taxon.latdist(occurrences.search(scientificname = "Mola mola", size=100).execute(), level="species", interactive=False).__clas__.__name__ == "AxesSubplot"

    fig = taxon.latdist(occurrences.search(scientificname = "Mola mola", size=100).execute(), level="species", interactive=True)
    assert fig.__class__.__name__ == "Figure"
