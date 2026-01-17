import pandas as pd
import matplotlib.pyplot as plt

# Veri yükleme
df = pd.read_csv("data/daily_sales.csv")

print("İlk 5 satır:")
print(df.head())

print("\nBilgi:")
print(df.info())

print("\nTanımlayıcı istatistikler:")
print(df.describe())

average_sales = df["sales"].mean()
print("\nOrtalama satış:", average_sales)

plt.figure()
plt.plot(df["day"], df["sales"], marker="o")
plt.axhline(y=average_sales, linestyle="--")
plt.title("Day05 – Daily Sales EDA")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/day05_eda_plots.png")
plt.show()

