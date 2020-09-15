import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('max_rows', 50000)
pd.set_option('max_columns', 7)
pd.set_option('display.width', 1000)


df=pd.read_csv(r"C:\Users\gcris\Documents\MEGA\MEGAsync\Programming\Python\Learning topics\Subito.it\houses1.csv",encoding='unicode_escape')
df = df.dropna()
# print(df.head())
def rem(x):
    return x[-5:]

df["data1"] = df["Date"].apply(lambda x: rem(x))

# print(df.date[-5:])
print(df.head(3))
df["data1"].hist(bins=20)
plt.show()
df.to_csv("houses_freq.csv")