import pandas as pd
import matplotlib.pyplot as plt
import os

# Dosya yolu
DATA_PATH = "data/daily_sales.csv"
OUTPUT_DIR = "visuals"

# Klasör yoksa oluştur
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Veriyi oku
df = pd.read_csv(DATA_PATH)

print("İlk 5 satır:")
print(df.head())

print("\nTanımlayıcı istatistikler:")
print(df.describe())

# Günlük satış grafiği
plt.figure()
plt.plot(df["day"], df["sales"], marker="o")
plt.title("Günlük Satışlar")
plt.xlabel("Gün")
plt.ylabel("Satış")
plt.grid(True)

output_path = os.path.join(OUTPUT_DIR, "daily_sales_step2.png")
plt.savefig(output_path)
plt.close()

print(f"\nGrafik kaydedildi: {output_path}")





