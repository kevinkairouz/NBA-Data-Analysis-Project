import pandas as pd   
import matplotlib as plt 

def searchPlayerStats(playerName): 

    dataSet = pd.read_csv("nbaNew.csv")    
    d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()   

    d["PPG"] = d["PTS"]/d["G"]  
    d["RPG"] = d["TRB"]/d["G"]  
    d["APG"] = d["AST"]/d["G"]  

    print(d.loc[playerName][["PPG", "RPG", "APG"]]) 
    print(f"{searchPlayer} has played for the following") 
    teamQuery = dataSet[dataSet["PlayerName"] == playerName]  
    print(teamQuery[["Tm"]].drop_duplicates())  
    return 

def findTopFive():  
    dataSet = pd.read_csv("nbaNew.csv")    
    d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()   

    d["PPG"] = d["PTS"]/d["G"]  
    d["RPG"] = d["TRB"]/d["G"]  
    d["APG"] = d["AST"]/d["G"]  

    d = d.sort_values(by=["PPG", "RPG", "APG"], ascending= False)    
    print(d.head()) 

def findWorstFive(): 
    dataSet = pd.read_csv("nbaNew.csv")    
    d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()   

    d["PPG"] = d["PTS"]/d["G"]  
    d["RPG"] = d["TRB"]/d["G"]  
    d["APG"] = d["AST"]/d["G"]  

    d = d.sort_values(by=["PPG", "RPG", "APG"], ascending= False)    
    print(d.tail())




print("Welcome to the NBA player finder")
searchPlayer = str(input("Enter an NBA player: "))  

searchPlayerStats(searchPlayer)

















