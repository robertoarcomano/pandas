import pandas as pd


ps = pd.Series([1, 2, 3])
print(ps)

df = pd.DataFrame()
df["Close"] = [1000, 2000, 3000]
df["Open"] = [100, 200, 300]
print(df)

df1 = pd.DataFrame({"a": ps})
df1["timestamp"] = pd.Timestamp("now")
df1["n"] = 2
print(df1)
print(df1.dtypes)

