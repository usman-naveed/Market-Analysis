from ta import momentum
import pandas as pd


class FeatureEngineering:
    """ Feature Engineering class that adds TA's to the caller object's dataframe.
        Use function add_all() to add all indicators, or add them individually by calling funcs below.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def add_rsi(self) -> pd.DataFrame:
        rsi = momentum.rsi(self.df['close'], fillna=True)
        self.df['RSI'] = rsi
        return self.df

    def add_ao(self) -> pd.DataFrame:
        # TODO: Figure out int parameters
        ao = momentum.ao(self.df['high'], self.df['low'], fillna=True)
        self.df['AO'] = ao
        return self.df

    def add_kama(self) -> pd.DataFrame:
        # TODO: Figure out (int parameters)
        kama = momentum.kama(self.df['close'], fillna=True)
        self.df['KAMA'] = kama
        return self.df

    def add_roc(self) -> pd.DataFrame:
        # TODO: Figure out (int parameters)
        roc = momentum.roc(self.df['close'], fillna=True)
        self.df['ROC'] = roc
        return self.df

    def add_stoch(self) -> pd.DataFrame:
        # TODO: Figure out (int parameters)
        stoch = momentum.stoch(self.df['high'], self.df['low'], self.df['close'], fillna=True)
        sig_stoch = momentum.stoch_signal(self.df['high'], self.df['low'], self.df['close'], fillna=True)
        self.df['STOCH'] = stoch
        self.df['SIG_STOCH'] = sig_stoch
        return self.df

    def add_tsi(self) -> pd.DataFrame:
        # TODO: Figure out (int parameters)
        tsi = momentum.tsi(self.df['close'], fillna=True)
        self.df['TSI'] = tsi
        return self.df

    def add_uo(self) -> pd.DataFrame:
        # TODO: Figure out (int parameters)
        uo = momentum.uo(self.df['high'], self.df['low'], self.df['close'], fillna=True)
        self.df['UO'] = uo
        return self.df

    def add_wr(self) -> pd.DataFrame:
        # TODO: Figure out (int parameters)
        wr = momentum.wr(self.df['high'], self.df['low'], self.df['close'], fillna=True)
        self.df['WR'] = wr
        return self.df

    def add_all(self) -> pd.DataFrame:
        self.add_rsi()
        self.add_ao()
        self.add_uo()
        self.add_wr()
        self.add_kama()
        self.add_roc()
        self.add_stoch()
        self.add_tsi()
        return self.df
