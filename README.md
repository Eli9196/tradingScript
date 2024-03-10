# tradingScript
<!DOCTYPE html>
<html>
<head>
  <title>ATR Trailing Stop Strategy</title>
</head>
<body>
  <h1>ATR Trailing Stop Strategy</h1>

  <p>This Python script implements an Average True Range (ATR) trailing stop strategy for trading. The strategy calculates the ATR based on historical price data and uses it to determine the trailing stop level for buying and selling signals.</p>

  <h2>Features</h2>
  <ul>
    <li>Calculates ATR based on a specified length</li>
    <li>Calculates nLoss (ATR * sensitivity) for determining trailing stop</li>
    <li>Determines buy and sell signals based on the trailing stop level</li>
  </ul>

  <h2>Usage</h2>
  <ol>
    <li>Replace the <code>data</code> dictionary with your historical price data.</li>
    <li>Set the <code>length</code> and <code>sensitivity</code> parameters for the ATR calculation.</li>
    <li>Run the script to generate buy and sell signals.</li>
  </ol>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>NumPy</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
