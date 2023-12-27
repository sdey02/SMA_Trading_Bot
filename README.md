# Background
With a intrest in Quant and furthering my python abilites I have taken up the project of building a simple SMA trading bot. Attached below will be the research and a general overview of what the bot looks for and how it works.

# High Level Overview
<h4>What is SMA?</h4>
SMA or Simple Moving Average is the average closing price of a stock over a certain amount of days. The most common simple moving averages used for a stock are 10, 20, 50, 100 and 200 days.

<h4>Why is it usefull?</h4>
SMA can help us decide reduce the noise of the market and tell us wether a certain stock is worth buying or selling at any given times. To figure this out we need to know if the stock is in an uptrend or downtrend.

<h4>How to know if the stock price is in an uptrend?</h4>
If the current price has stayed above the moving average for a while the price is said to be in an uptrend. For a general view of a stock we check the current price to the 50 day moving average and if both are increasing we can say the stock as a whole is in an uptrend. As traders we wnat to look for sell opporuntities to maximize our profits.

<h4>How to know if the stock price is in an downtrend?</h4>
If the current price has stayed below the moving average for a while the price is said to be in an downtrent Again as in the case of an uptrend for a general view of a stock  we check the current price to the 50 day moving average and if the current price is below the 50 day sma and both are falling we can say the stock as a whole is in an downtrend. As traders we wnat to look for buy opporuntities to buy low before the stock enters an uptrend to maximize our profits.

<h4>How to know if there is no trend to a stock price??</h4>
If the current price has fluctuates like a pendulum around the moving average for a while the price is in an sidweways trend. Generally herre we want to stay away but if we want to take some risks we can try to predict when we are at the bottom of the swing so we can buy and consequently sell when we are at the top of the swing.


