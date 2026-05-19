import pandas as pd

df = pd.read_csv("sales2019.csv")

# explore dataset
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

# remove unnecessary columns
df.drop(columns=["promo_bin_2", "promo_discount_2", "promo_type_2"], inplace=True)

# replace missing values in promo_bin_1 with "no promo"
df["promo_bin_1"] = df["promo_bin_1"].fillna("No Promo")

# save cleaned dataset
df.to_csv("sales2019_cleaned.csv", index=False)

print("Dataset cleaned successfully")
