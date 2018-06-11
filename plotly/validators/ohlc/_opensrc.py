import _plotly_utils.basevalidators


class OpensrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(self, plotly_name='opensrc', parent_name='ohlc', **kwargs):
        super(OpensrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )