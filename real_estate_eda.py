# import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv("/Users/maram/Maram/dsndml/week1/world_real_estate_data(147k).csv")

# preview the head to get an idea o fthe dataset
print("preview the head"+ df.head())

# print the dataset shape rows x columns
print("dataset shape" + df.shape)

sns.set(style="whitegrid")


# 1. Number of distinct countries
print("\nDistinct countries:", df["country"].nunique())

# 2. Properties per country
properties_per_country = df["country"].value_counts()
print("\nProperties per Country:\n", properties_per_country)

plt.figure(figsize=(12, 5))
properties_per_country.head(15).plot(kind="bar", color="mediumpurple")
plt.title("Top 15 Countries by Property Count")
plt.xlabel("Country")
plt.ylabel("Number of Properties")
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Group construction years in 5 from 2000 year
year_bins = list(range(2000, 2026, 5))  # 2000–2025 in steps of 5
year_labels = [f"{y}-{y+4}" for y in year_bins[:-1]]

df_filtered_years = df[df["building_construction_year"].between(2000, 2025, inclusive='both')].copy()
df_filtered_years["year_group"] = pd.cut(
    df_filtered_years["building_construction_year"],
    bins=year_bins,
    labels=year_labels,
    right=False  
)

year_group_counts = df_filtered_years["year_group"].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 4))
year_group_counts.plot(kind="bar", color="deepskyblue")
plt.title("Properties Grouped by 5-Year Construction Ranges (2000–2025)")
plt.xlabel("Construction Year Range")
plt.ylabel("Number of Properties")
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# 4. Properties by total building floors
plt.figure(figsize=(10, 4))
sns.countplot(x="building_total_floors", data=df, palette="Greens_d",
              order=df["building_total_floors"].value_counts().index)
plt.title("Properties by Total Building Floors")
plt.xlabel("Number of Floors")
plt.ylabel("Count")
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 5. Properties by apartment floor
plt.figure(figsize=(10, 4))
sns.countplot(x="apartment_floor", data=df, palette="Reds_d",
              order=df["apartment_floor"].value_counts().index)
plt.title("Properties by Apartment Floor")
plt.xlabel("Apartment Floor")
plt.ylabel("Count")
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 6. Price Distribution (10K–1M)
price_bins = pd.cut(df["price_in_USD"], bins=np.arange(10000, 1_000_000 + 100000, 100000))
price_distribution = price_bins.value_counts().sort_index()

plt.figure(figsize=(12, 5))
price_distribution.plot(kind="bar", color="orchid")
plt.title("Price Distribution (USD 10K to 1M)")
plt.xlabel("Price Range")
plt.ylabel("Number of Properties")
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
