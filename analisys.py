import pandas as pd

pd.set_option('max_rows', 50000)
pd.set_option('max_columns', 7)
pd.set_option('display.width', 1000)


df=pd.read_csv("cars.csv",encoding= 'unicode_escape')
df = df.dropna()

def rem(x):
    return x[-5:]

df["data1"] = df["date"].apply(lambda x: rem(x))

# print(df.date[-5:])
print(df)