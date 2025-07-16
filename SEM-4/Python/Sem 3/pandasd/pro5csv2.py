import pandas as pd
mydataset = {
 'country': ["India", "Japan", "Dubai"],
 'State': [1,2,3]
 }
df = pd.DataFrame(mydataset)
print(df.to_csv('outputfile.csv',index=False))