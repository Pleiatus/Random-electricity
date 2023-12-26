import numpy as np
import pandas as pd
from datafixer import *
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
price=elefixer(pd.read_csv("2020.csv"))
weather = weatherfixer(pd.read_csv("HV2020.csv", dtype={
    "Vuosi": "string",
    "Kuukausi": "string",
    "Päivä": "string",
    "Aika [Paikallinen aika]": "string"
}))
weather["Lämpötilan keskiarvo [°C]"]=pd.to_numeric(weather["Lämpötilan keskiarvo [°C]"], errors='coerce')
weather["Keskituulen nopeus [m/s]"]=pd.to_numeric(weather["Keskituulen nopeus [m/s]"], errors='coerce')
weather["Ilmanpaineen keskiarvo [hPa]"]=pd.to_numeric(weather["Ilmanpaineen keskiarvo [hPa]"], errors='coerce')
data=price.merge(weather, how="left", on="time")
print(data)
Y=data["Day-ahead Price [EUR/MWh]"].interpolate()
X=data.drop(columns=["Day-ahead Price [EUR/MWh]","time"]).interpolate()
for i in range(len(Y)):
    print(Y[i])

