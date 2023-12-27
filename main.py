import numpy as np
import math
import polars as pl
import yahoo_fin; from yahoo_fin import stock_info as si

stocks = pl.read_csv("sp_500_stocks.csv")

final_dataframe = pl.DataFrame(
    {
        "Ticker": [],
        "30 day Trend": [],
        "Current Trend": [],
        "Market Capitalization": [], 
        "Number of Shares to Buy": [],
    }
)
