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