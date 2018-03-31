import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style #style package allows customizable

style.use('ggplot')

def ticker_lookup():
    '''
        This function will look up a ticker symbol from Morningstar database
        in a desired period.
    '''
    ticker = input('Enter ticker symbol: ')
    start_date = input('Enter start date in YYYY-MM-DD format: ')
    end_date = input('Enter End date in YYYY-MM-DD format: ')
    s_year,s_month,s_day = map(int, start_date.split('-'))
    e_year,e_month,e_day = map(int, end_date.split('-'))
    start=dt.datetime(s_year,s_month,s_day)
    end=dt.datetime(e_year,e_month,e_day)

    #extracting data from morningstar financial to make our dataframe
    df_value = web.DataReader(ticker, "morningstar", start, end)
    return df_value

def stockPrice_MA_plot(df_value):
    '''
        def stockPrice_MA_plot(df_val):

        This will return a graph of stock price and moving average

    '''
    df = df_value
    df.index = df.index.get_level_values('Date')   #our data has multi-level index so we only set date as our index
    df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean() #computing 100 moving average using rolling

    ax1 = plt.subplot2grid((7, 1), (1, 0), rowspan=5, colspan=1)
    plt.title("Daily Stock Price & Moving Average")
    ax2 = plt.subplot2grid((7, 1), (6, 0), rowspan=1, colspan=1, sharex=ax1)
    ax1.plot(df.index, df['Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])
    plt.show()

def candlestick_plot(df_value, period):
    '''

        def candlestick_plot(df_value, period):

        This will return a candlestick plot with the option of select the period of each candlestick.
        Green candlestick means price went up for that day and red candlestick means price went down.

        Input variable:
        period - how many weeks or days or minutes will the candlestick be (e.g. 10D = 10 days, 10Min = 10 minutes)
    '''
    from matplotlib.finance import candlestick_ohlc
    import matplotlib.dates as mdates

    df = df_value

    df_ohlc = df['Close'].resample(period).ohlc()
    df_volume = df['Volume'].resample(period).sum()

    df_ohlc = df_ohlc.reset_index()  # reseting our index, date is no longer our index
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
    #fig = plt.figure()
    ax1 = plt.subplot2grid((7, 1), (1, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((7, 1), (6, 0), rowspan=1, colspan=1, sharex=ax1)
    ax1.xaxis_date()

    candlestick_ohlc(ax1, df_ohlc.values, width=4, colorup='g')
    ax2.fill_between(df_volume.index.map(mdates.date2num),
                     df_volume.values, 0)
    plt.show()