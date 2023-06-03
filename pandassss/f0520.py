import pandas as pd

data = pd.DataFrame({
    "name":["amy","john","bob"],
    "salary":[30000,40000,300]
})
print(data)
print(data.shape)
s1 = pd.Series