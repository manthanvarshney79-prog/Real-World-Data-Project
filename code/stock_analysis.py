import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../dataset/AAPL.csv")

print("First 5 Rows")
print(data.head())

print("\nDataset Information")
print(data.info())

print("\nStatistical Summary")
print(data.describe())

print("\nMissing Values")
print(data.isnull().sum())

avg_close = data["AAPL.Close"].mean()
max_close = data["AAPL.Close"].max()
min_close = data["AAPL.Close"].min()

print("\nAverage Closing Price:", avg_close)
print("Maximum Closing Price:", max_close)
print("Minimum Closing Price:", min_close)

plt.figure(figsize=(8, 4))
plt.plot(data["AAPL.Close"])
plt.title("Apple Stock Closing Price")
plt.xlabel("Days")
plt.ylabel("Price")
plt.savefig("../images/stock_price.png")
plt.close()

volume = data["AAPL.Volume"].head(10)

plt.figure(figsize=(8, 4))
volume.plot(kind="bar")
plt.title("Apple Trading Volume")
plt.xlabel("Records")
plt.ylabel("Volume")
plt.savefig("../images/trading_volume.png")
plt.close()

print("\nProject Completed Successfully")
