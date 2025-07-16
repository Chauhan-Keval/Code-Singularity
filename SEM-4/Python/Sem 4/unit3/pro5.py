import pandas as pd
df=pd.read_csv("demo.csv")
new_df = df.dropna()
print(new_df)
new_df.to_csv("new_demo.csv", index=False)