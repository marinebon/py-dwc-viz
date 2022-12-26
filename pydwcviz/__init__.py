"""
PyDwcViz Library

Example Usage:
# import the complete library
import pydwcviz

"""

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

__title__ = "pydwcviz"
__author__ = "Ayush Anand, Tylar Murray"
__license__ = "MIT"

__all__ = [
    "taxon",
    "stats",
    "diversity"
]