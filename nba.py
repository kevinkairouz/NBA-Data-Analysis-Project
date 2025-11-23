import pandas as pd   
import matplotlib as plt 

dataSet = pd.read_csv("nbaNew.csv")  


d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()   

d["PPG"] = d["PTS"]/d["G"]  
d["RPG"] = d["TRB"]/d["G"]  
d["APG"] = d["AST"]/d["G"]


d = d.sort_values(by=["PPG"], ascending= False)   

print(d[["PPG", "APG", "RPG"]].head())










