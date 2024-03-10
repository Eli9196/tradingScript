import numpy as np

# Define input parameters
length = 5
sensitivity = 2
heikin_ashi = False

# Calculate ATR
def calculate_atr(data, length):
    high = data['High']
    low = data['Low']
    close = data['Close']
    atr = np.zeros(len(close))
    for i in range(length, len(close)):
        tr = max(high[i] - low[i], abs(high[i] - close[i - 1]), abs(low[i] - close[i - 1]))
        atr[i] = (atr[i - 1] * (length - 1) + tr) / length
    return atr

# Calculate nLoss
def calculate_nloss(atr, sensitivity):
    return sensitivity * atr

# Define trailing stop logic
def calculate_trailing_stop(close, atr, nLoss):
    trailing_stop = np.zeros(len(close))
    for i in range(1, len(close)):
        if close[i] > trailing_stop[i - 1]:
            trailing_stop[i] = close[i] - nLoss
        else:
            trailing_stop[i] = close[i] + nLoss
    return trailing_stop

# Load historical price data (replace this with actual price data)
data = {
    'Open': np.random.rand(100),
    'High': np.random.rand(100),
    'Low': np.random.rand(100),
    'Close': np.random.rand(100)
}

# Calculate ATR
atr = calculate_atr(data, length)

# Calculate nLoss
nloss = calculate_nloss(atr, sensitivity)

# Calculate xATRTrailingStop (replace this with your logic)
xATRTrailingStop = calculate_trailing_stop(data['Close'], atr, nloss)

# Determine buy and sell signals
signals = np.zeros(len(data['Close']))
for i in range(1, len(data['Close'])):
    if data['Close'][i] > xATRTrailingStop[i] and data['Close'][i - 1] <= xATRTrailingStop[i - 1]:
        signals[i] = 1  # Buy signal
    elif data['Close'][i] < xATRTrailingStop[i] and data['Close'][i - 1] >= xATRTrailingStop[i - 1]:
        signals[i] = -1  # Sell signal

# Plot buy and sell signals (replace this with your plotting code)
for i in range(len(signals)):
    if signals[i] == 1:
        print(f'Buy signal at index {i}')
    elif signals[i] == -1:
        print(f'Sell signal at index {i}')
