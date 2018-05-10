### stock_price_graph

This is a finance project dealing with prediction of stock price using machine learning and some deep learning. All codes are in python. This package is an ongoing development as it needs to be implemented some machine learning and deep learning.

When this model is finished, it will be used to do paper-trading to test it's trading algorithm.

Files:

1. stock_price.py -- has ticker_lookup, stockPrice_MA_plot, and candlestick_plot function
    a. ticker_lookup function can be used to retrieve stock price over a period of trading: high, low, close, volume
    b. stockPrice_MA_plot function can be used to plot 100days moving average but it can be used to plot any period of moving average
    c. candlestick_plot function can be used to plot a candlestick chart
    
2. joined_data.py -- has one function called compile_data which can be used to the close price of all the stocks from a list so that it can be used to calculate the correlation between each other.

3. correlation.py -- has one function called correlation which can be used to calculate the correlation between each stock. If they are correlated, one can long an uptrending stock and short a down-trending stock.

*Note this is an ongoing project
