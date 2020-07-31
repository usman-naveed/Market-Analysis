import Cleaning.DataCleaning as dc
import Cleaning.FeatureEngineering as fe
import matplotlib.pyplot as plt
from heatmap import heatmap, corrplot

#Remove first row of DF? (cuz of bad values)

x = dc.Clean("~/PycharmProjects/stonkz/data/prices-split-adjusted.csv")
aapl = x.appl_df()
amzn = x.amzn_df()
msft = x.msft_df()

aapl = fe.FeatureEngineering(aapl).add_all()
plt.figure(figsize=(10,10))
corrplot(aapl.corr())
print(aapl.describe())
print(aapl.columns)

plt.plot(aapl['date'], aapl['close'], color='red')
plt.plot(aapl['date'], aapl['RSI'], color='green')
plt.hlines(70, 0, 2000)
plt.hlines(30, 0, 2000)
plt.show()
