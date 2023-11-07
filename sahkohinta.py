import pandas as pd
import numpy as np
df = pd.read_csv("2020.csv")
data = []
list=df.iloc[:,1]
for i in range(len(list)):
    if (i+16)%24<16:
        data.append(float(list[i]))
print(np.average(data))
