import sys

if sys.version_info < (3, 7):
    from ._stream import Stream
    from ._marker import Marker
    from ._hoverlabel import Hoverlabel
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".hoverlabel"],
        ["._stream.Stream", "._marker.Marker", "._hoverlabel.Hoverlabel"],
    )
