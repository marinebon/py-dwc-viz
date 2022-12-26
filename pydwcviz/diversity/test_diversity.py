"""
Tests for diversity module
"""
from pydwcviz import diversity
from pyobis import occurrences

def test_shannon_obis():
    """Testing calculation of shannon's index using OBIS Data"""
    data = occurrences.search(
        # this is a geometry in the Arabian Sea
        geometry="POLYGON ((58.3301 19.0935, 69.8145 19.0381, 69.8145 9.5161, 58.6230 9.6316, 58.3301 19.0935))",
        size = 500,
    ).execute()

    assert diversity.shannon(data, 3).__class__.__name__ == "DataFrame"

def test_es50_obis():
    """Testing calculation of ES50 (Hulbert's) index using OBIS Data"""
    data = occurrences.search(
        # this is a geometry in the Arabian Sea
        geometry="POLYGON ((58.3301 19.0935, 69.8145 19.0381, 69.8145 9.5161, 58.6230 9.6316, 58.3301 19.0935))", 
        size = 500,
    ).execute()

    assert diversity.es50(data, 3).__class__.__name__ == "DataFrame"