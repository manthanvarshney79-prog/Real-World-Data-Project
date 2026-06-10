import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../dataset/AAPL.csv")

print(data.head())

print("\nDataset Information")
print(data.info())

print("\nStatistical Summary")
print(data.describe())

plt.figure(figsize=(8,5))
plt.plot(data["Close"])
plt.title("Apple Stock Closing Prices")
plt.xlabel("Days")
plt.ylabel("Price")
plt.savefig("../images/stock_price_trend.png")
plt.close()

print("\nAverage Closing Price:")
print(data["Close"].mean())

print("\nProject Completed Successfully")
