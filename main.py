import backtrader as bt
import yfinance as yf
import matplotlib


apple = yf.download(tickers='AAPL') # Get Stock data from yf

apple_parsed = bt.feeds.PandasData(dataname = apple) # Parse YF data for cerebro engine


class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast = 50,  # period for the fast moving average
        pslow = 200,   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period = self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period = self.p.pslow)  # slow moving average

        self.crossover_50_200 = bt.ind.CrossOver(sma1, sma2)  # crossover signal
        self.MACD = bt.ind.MACD() # MCAD Line

    def next(self):
        if not self.position:  # not in the market
            if self.crossover_50_200 > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover_50_200 < 0:  # in the market & cross to the downside
            self.close()  # close long position

cerebro = bt.Cerebro() # Initiate the Cerebro Engine

cerebro.adddata(apple_parsed) # Load Historical Data

cerebro.broker.setcash(100.0) # Set Starting Cash

cerebro.addstrategy(SmaCross) # Load Strategy

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue()) # Print out the starting value of portfolio

cerebro.run() # Run Engine

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue()) # Print out the final value of portfolio

print(cerebro.plot())