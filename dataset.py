import pandas as pd

data = pd.read_csv("ageutk_full.csv")

def df_range(df, min_val, max_val):
    return df[(min_val <= df.age) & (df.age <= max_val)]


rangedAgeData = df_range(data,0, 70)
print(rangedAgeData)