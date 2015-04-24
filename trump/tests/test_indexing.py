from ..indexing import DatetimeIndexImp

from pandas.util.testing import assert_series_equal, assert_frame_equal

class TestIndexImplementers(object):

    def test_datetime_index_imp(self):

        dii = DatetimeIndexImp(...)

    def test_integer_index_imp(self):

        iii = IntIndexImp(...)

    def test_string_index_imp(self):

        sii = StringIndexImp(...)

    def test_period_index_imp(self):

        pii = PeriodIndexImp(...)