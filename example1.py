import pandas as pd


ps = pd.Series([1, 2, 3])
print(ps)
print()

df = pd.DataFrame({"Close": [1000, 2000, 3000]})
df["Open"] = [100, 200, 300]
print(df)
print()

df["a"] = ps
df["timestamp"] = pd.Timestamp("now")
df["n"] = 2
print(df)
print()

print(df.dtypes)
print()

print(df.head(1))
print()

print(df[0:2])
print()

print(df.loc[df["Open"]>100,"Open"])
print()

print(df.describe())
print()

