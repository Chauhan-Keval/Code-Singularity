import pandas as pd
df=pd.read_csv('car_price_dataset.csv').loc[0:100]
print(df)
