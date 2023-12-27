import numpy as np
import math
import polars as pl
import yahoo_fin; from yahoo_fin import stock_info as si

stocks = pl.read_csv("sp_500_stocks.csv")

final_dataframe = pl.DataFrame(
    {
        "Ticker": [],
        "Buy or Sell?": [], 
        "Current Price": [],
        "20 Day Trend": [],
        "50 Day Trend": [],
        "200 Day Trend": [],
        "Current Trend": [],
    }
)

trend_dataframe = pl.DataFrame(
    {
        "Ticker": [],
        "Uptrend Counter": [],
        "Downtrend Counter": [],
    }
)

final_dataframe = final_dataframe.with_columns(
    [
        pl.col("Ticker").cast(pl.Utf8),
        pl.col("Buy or Sell?").cast(pl.Utf8),
        pl.col("Current Price").cast(pl.Float64),
        pl.col("20 Day Trend").cast(pl.Float64),
        pl.col("50 Day Trend").cast(pl.Float64),
        pl.col("200 Day Trend").cast(pl.Float64),
        pl.col("Current Trend").cast(pl.Utf8),
    ]
)

for stock in stocks['Ticker'][:5]:
    twenty_day_sma = yahoo_fin.stock_info.get_data(stock, interval='1d')['close'][-20:].mean()
    fifty_day_sma = yahoo_fin.stock_info.get_data(stock, interval='1d')['close'][-50:].mean()
    two_hundred_day_sma = yahoo_fin.stock_info.get_data(stock, interval='1d')['close'][-200:].mean()
    price = yahoo_fin.stock_info.get_live_price(stock)

    stock_info = pl.DataFrame(
        {
            "Ticker": [stock],
            "Buy or Sell?": ['N/A'], 
            "Current Price": [price],
            "20 Day Trend": [twenty_day_sma],
            "50 Day Trend": [fifty_day_sma],
            "200 Day Trend": [two_hundred_day_sma],
            "Current Trend": ['N/A'],
        }
    )

    final_dataframe = pl.concat([final_dataframe, stock_info])


print(final_dataframe)
