import pandas as pd
class panduram():
    def __init__(self,read):
        self.read=pd.read_csv("demo.csv")
    def show(self):
        print(self.read)
read="demo"
obj=panduram(read)
obj.show()
        
        
