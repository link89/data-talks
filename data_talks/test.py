import unittest
import akshare as ak


class TestAkshare(unittest.TestCase):
    def test_load_topx(self):
        topx_df = ak.index_investing_global(
            country="日本", index_name="日本东证指数", period="每日",
            start_date="2020-01-01", end_date="2020-10-01"
        )
        print(topx_df)
