import pandas as pd
import matplotlib.pyplot as plt

# Veri setini yükle
df = pd.read_csv("data/daily_sales.csv")

# Veri tipini garantiye al
df["sales"] = df["sales"].astype(int)

# İlk 5 satır
print("İlk 5 satır:")
print(df.head())


# Ortalama satış
average_sales = df["sales"].mean()
print("\nOrtalama satış:", average_sales)

# Ortalama üstü mü?
df["above_average"] = df["sales"] > average_sales

print("\nGünlere göre ortalama üstü durumu:")
print(df[["day", "sales", "above_average"]])

# Groupby ile özet
summary = df.groupby("above_average")["sales"].agg(
    count="count",
    mean="mean",
    max="max",
    min="min"
)

print("\nGroupby özeti:")
print(summary)

# Ortalama satış karşılaştırma grafiği
plt.figure(figsize=(6, 4))
summary["mean"].plot(kind="bar")
plt.title("Average Sales Comparison")
plt.ylabel("Sales")
plt.tight_layout()

# Grafiği kaydet
plt.savefig("visuals/average_sales_comparison.png")
plt.show()

print("\nGrafik kaydedildi: visuals/average_sales_comparison.png")

"""
INSIGHT:
- Ortalama üstü günlerde satış ortalaması belirgin şekilde daha yüksektir
- Satışların az sayıda günde yoğunlaştığı görülmektedir
- Bu durum kampanya, özel gün veya talep artışı ile açıklanabilir
"""

