import pandas as pd 
mydataset = {
    'cars':["BMW","Volvo","Ford"],
    'passing':[3,7,5]
}
a = pd.DataFrame(mydataset)
print(a)