"""
Tests for stats module
"""
from pydwcviz import stats

def test_get_records():
    """Testing response type and request for statistics/records"""
    res = stats.get_records(taxonid=1363)
    assert res.__class__.__name__ == "dict"

def test_get_qc():
    """Testing response type and request for statistics/qc"""
    res = stats.get_qc(taxonid=1363)
    assert res.__class__.__name__ == "dict"

def test_get_env():
    """Testing response type and request for statistics/env"""
    res = stats.get_years(taxonid=1363)
    assert res.__class__.__name__ == "list"

def test_get_years():
    """Testing response type and request for statistics/years"""
    res = stats.get_env(taxonid=1363)
    assert res.__class__.__name__ == "dict"

def test_get_composition():
    """Testing response type and request for statistics/composition"""
    res = stats.get_composition(taxonid=1363)
    assert res.__class__.__name__ == "dict"

def test_dist_years():
    """Test time distriution of records function - both interactive and non-interactive"""
    assert stats.dist_years(stats.get_years(taxonid = 1071), interactive=False).__class__.__name__ == "AxesSubplot"

    fig = stats.dist_years(stats.get_years(taxonid = 1071), interactive=True)
    assert fig.__class__.__name__ == "Figure"
    
def test_dist_env():
    """Test time distriution of records function - both interactive and non-interactive"""
    assert stats.dist_env(stats.get_env(taxonid = 1071), parameter="sst", interactive=False).__class__.__name__ == "AxesSubplot"

    fig = stats.dist_env(stats.get_env(taxonid = 1071), parameter="depth", interactive=True)
    assert fig.__class__.__name__ == "Figure"