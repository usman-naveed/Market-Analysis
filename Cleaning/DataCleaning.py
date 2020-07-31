import pandas as pd

# TODO: Add more methods for other tickers


class Clean:
    """ Cleaning class that implements methods to read the raw csv, or return specific ticker dataframes for
    processing tasks."""
    def __init__(self, path):
        self.__path = path
        self.df = pd.read_csv(self.__path)

    def read_csv(self):
        return pd.read_csv(self.__path)

    def set_path(self, new_path):
        self.__path = new_path

    def get_path(self) -> str:
        return self.__path

    def appl_df(self) -> pd.DataFrame:
        return self.df[self.df['symbol'] == 'AAPL'].reset_index(drop=True)

    def msft_df(self) -> pd.DataFrame:
        return self.df[self.df['symbol'] == 'MSFT'].reset_index(drop=True)

    def amzn_df(self) -> pd.DataFrame:
        return self.df[self.df['symbol'] == 'AMZN'].reset_index(drop=True)

    def fb_df(self) -> pd.DataFrame:
        return self.df[self.df['symbol'] == 'FB'].reset_index(drop=True)

    def intc_df(self) -> pd.DataFrame:
        return self.df[self.df['symbol'] == 'INTC'].reset_index(drop=True)