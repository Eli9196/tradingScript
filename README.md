# tradingScript
#ATR Trailing Stop Strategy
This Python script implements an Average True Range (ATR) trailing stop strategy for trading. The strategy calculates the ATR based on historical price data and uses it to determine the trailing stop level for buying and selling signals.

#Features
Calculates ATR based on a specified length
Calculates nLoss (ATR * sensitivity) for determining trailing stop
Determines buy and sell signals based on the trailing stop level
#Usage
Replace the data dictionary with your historical price data.
Set the length and sensitivity parameters for the ATR calculation.
Run the script to generate buy and sell signals.
#Requirements
Python 3.x
NumPy
