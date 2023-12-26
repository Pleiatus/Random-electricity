import numpy as np
import pandas as pd
def elefixer(df):
    timecheck= df["MTU (CET/CEST)"]
    last = 23
    for i in timecheck:
        if (last+1)%24 != int(i[11:13]):
            print("duplicate or missing elements at")
            print(i)
            print("if output long missing elements, none spotted so far")
        last = int(i[11:13])
    df.drop_duplicates(subset=["MTU (CET/CEST)"], inplace=True)
    df["time"]=df.apply(lambda row: row["MTU (CET/CEST)"][0:2]+row["MTU (CET/CEST)"][3:5]+row["MTU (CET/CEST)"][6:10]+row["MTU (CET/CEST)"][11:13],axis=1)
    df=df.drop(columns=["MTU (CET/CEST)","Currency","BZN|FI"])
    return df
def weatherfixer(df):
    df["time"]=df.apply(lambda row: row["Päivä"]+str(row["Kuukausi"])+str(row["Vuosi"])+str(row["Aika [Paikallinen aika]"])[0:2],axis=1)
    df=df.drop(columns=["Havaintoasema","Vuosi","Kuukausi","Päivä","Aika [Paikallinen aika]"])
    return df
