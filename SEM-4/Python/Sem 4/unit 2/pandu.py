import pandas as pd
dict1 = {"name":['AAA','BBB','CCC','DDD','EEE'],
         "marks":[10,20,30,40,50],
         "city":['ZZZ','YYY','XXX','none','FFF']
        }
df = pd.DataFrame(dict1)
print(df)
df.to_csv("demo1.csv")
abc=pd.read_csv("demo.csv")
print(abc)
