"""
Ideally, we wouldn't need to pull in all the calc symbols here,
but courses were using 'import calc', so we need this for
backwards compatibility
"""
from importlib.metadata import PackageNotFoundError, version

from .calc import *

try:
    __version__ = version("openedx-calc")
except PackageNotFoundError:  # pragma: no cover
    # Only hit if this package is imported without being installed at all
    # (e.g. run directly from a source checkout with no metadata available).
    pass
