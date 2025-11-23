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

    yearQuery = dataSet[dataSet["PlayerName"] == playerName]  
    rookieYear = yearQuery["SeasonStart"].min() 
    finalYear = yearQuery["SeasonStart"].max() 
    yearsPlayed = yearQuery["SeasonStart"].count()    

    print(f"{playerName} was in the NBA for a total of {yearsPlayed} years from {rookieYear} to {finalYear}")
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

def compareTwoPlayers():  
    #TODO reuse function code and then do side by side comparison and have a input that asks for visulizaton 
    #and then use matplotlib 
    return


#function ideas: --> 

#function that chooses two random players in the db/dataset and u choose which player u rather have on ur team 
#after you get the reveal of the players 

#function that compares 3 players  

#function that shows a players minutes and compares it to a real game like minutes played vs rest 

#function that tracks a players points or minutes over the years we have access to age variable in csv 

#starting 5 function where you choose your starting 5 and another person chooses their starting 5 and u see who wins 

#same thing but 3 on 3 version 

#create stat called most offensive impact and find the most offensive impactful person  
#formula will be points + rebounds + assists - turnovers  

#same thing but defense 
#blocks + steals - fouls   

#show me a draft class 
#where we group by names and we choose the people who have the min year and if it is equal to draft class number user enters we display 
#those said players 



print("Welcome to the NBA player finder")
searchPlayer = str(input("Enter an NBA player: "))  

searchPlayerStats(searchPlayer)

















