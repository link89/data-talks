from unittest import TestCase
import akshare as ak
import investpy


class TestAkshare(TestCase):
    def test_load_topx(self):
        df = ak.index_investing_global(
            country="日本", index_name="日本东证指数", period="每日",
            start_date="2020-01-01", end_date="2020-10-01"
        )
        print(df.to_string())

    def test_load_fund_names(self):
        df = ak.fund_em_fund_name()
        print(df.to_string())

    def test_load_fund_data(self):
        df = ak.fund_em_open_fund_info(fund="000217", indicator="单位净值走势")
        print(df.to_string())


class TestInvest(TestCase):
    def test_get_indices_by_country(self):
        df = investpy.indices.get_indices('japan')
        print(df.to_string())

    def test_load_topx(self):
        df = investpy.indices.get_index_historical_data(
            index='Topix 1000',
            country='japan',
            from_date='01/01/2021',
            to_date='01/06/2021')
        print(df)


