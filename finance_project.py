# Finance Data Project 

# We'll focus on bank stocks and see how they progressed throughout the [financial crisis](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308) all the way to early 2016.

# *Note: [You'll need to install pandas-datareader for this to work!](https://github.com/pydata/pandas-datareader) Pandas datareader allows you to [read stock information directly from the internet](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) Use these links for install guidance (**pip install pandas-datareader**), or just follow along with the video lecture.

## Data

# We need to get data using pandas datareader. We will get stock information for the following banks:
# *  Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo

# ** Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:**
# 1. Use datetime to set start and end datetime objects.
# 2. Figure out the ticker symbol for each bank.
# 2. Figure out how to use datareader to grab info on the stock.

# ** Use [this documentation page](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html) for hints and instructions (it should just be a matter of replacing certain values. Use google finance as a source, for example:**
    
#     # Bank of America
#     BAC = data.DataReader("BAC", 'google', start, end)

### WARNING: MAKE SURE TO CHECK THE LINK ABOVE FOR THE LATEST WORKING API. "google" MAY NOT ALWAYS WORK. 

from pandas_datareader import data, wb
import pandas_datareader.data as web
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

start = datetime(2006, 1, 1)
end = datetime(2016, 1, 1)

# Bank of America
BAC = yf.download("BAC", start, end)

# CitiGroup
C = yf.download("C", start, end)

# Goldman Sachs
GS = yf.download("GS",start, end)

# JPMorgan Chase
JPM = yf.download("JPM",start, end)

# Morgan Stanley
MS = yf.download("MS",start, end)

# Wells Fargo
WFC = yf.download("WFC",start, end)

df = yf.download(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],start, end)

# ** Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers**

tickers=['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

# ** Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list. Also pay attention to what axis you concatenate on.**

bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)

# ** Set the column name levels:**

bank_stocks.columns.names = ['Bank Ticker','Stock Info']

# ** Check the head of the bank_stocks dataframe.**

fin=bank_stocks.head()
# print(fin)

# ** What is the max Close price for each bank's stock throughout the time period?**

fin=bank_stocks.xs("Close", level=1, axis=1).max()
# print(fin)

# ** Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock. returns are typically defined by:**

# $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$

returns=pd.DataFrame()

# ** We can use pandas pct_change() method on the Close column to create a column representing this return value. Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.**

for tick in tickers:
    returns[tick+" Return"]=bank_stocks[tick]["Close"].pct_change()
# print(returns.head())

# ** Create a pairplot using seaborn of the returns dataframe. What stock stands out to you? Can you figure out why?**

sns.pairplot(returns[1:])
# plt.show()

# ** Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns. You should notice that 4 of the banks share the same day for the worst drop, did anything significant happen that day?**

fin=returns.idxmin()
# print(fin)

# ** You should have noticed that Citigroup's largest drop and biggest gain were very close to one another, did anythign significant happen in that time frame? **

fin=returns.idxmax()
# print(fin)

# ** Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire time period? Which would you classify as the riskiest for the year 2015?**

# fin=returns.std() # all time std
fin=returns.loc['2015-01-01':'2015-12-31'].std() 
# print(fin)

# ** Create a distplot using seaborn of the 2015 returns for Morgan Stanley **

fin=returns.loc["2015-01-01":"2015-12-31"]["MS Return"]
sns.distplot(fin,bins=100,color="green") 
# plt.show()

# ** Create a distplot using seaborn of the 2008 returns for CitiGroup **

fin=returns.loc["2008-01-01":"2008-12-31"]["C Return"]
sns.distplot(fin,bins=100,color="red") 
# plt.show()

# More Visualization

import pandas as pd
import numpy as np
from plotly import __version__
import cufflinks as cf
import chart_studio.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.express as px
import pandas_ta as ta
import plotly.graph_objs as go
pyo.init_notebook_mode(connected=True)
cf.go_offline()

# ** Create a line plot showing Close price for each bank for the entire index of time. (Hint: Try using a for loop, or use [.xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html) to get a cross section of the data.)**

# <matplotlib.legend.Legend at 0x11cc896d8>

plt.figure(figsize=(12, 4))
fin = bank_stocks.xs('Close', axis=1, level=1)
label1=bank_stocks.columns.get_level_values(0).unique()
plt.plot(fin,label=label1)
plt.legend()
# plt.show()
# or
"""for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()
plt.show()"""

# <matplotlib.axes._subplots.AxesSubplot at 0x11d1aea58>

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()
# plt.show()

# interactive display

fig=bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot(asFigure=True)
# pyo.plot(fig)

# ** Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008**

plt.figure(figsize=(12,6))
BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()
# plt.show()

# ** Create a heatmap of the correlation between the stocks Close Price.**

sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
# plt.show()

# ** Optional: Use seaborn's clustermap to cluster the correlations together:**

sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
# plt.show()

# ** Use .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.**

fig=BAC[['Open', 'High', 'Low', 'Close']].loc['2015-01-01':'2016-01-01'].iplot(kind='candle',asFigure=True)
# pyo.plot(fig)

# ** Use .ta_plot(study='sma') to create a Simple Moving Averages plot of Morgan Stanley for the year 2015.**

fig=MS['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages',asFigure=True)
# pyo.plot(fig)

# **Use .ta_plot(study='boll') to create a Bollinger Band Plot for Bank of America for the year 2015.**

fig=BAC['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll',asFigure=True)
# pyo.plot(fig)











 

















