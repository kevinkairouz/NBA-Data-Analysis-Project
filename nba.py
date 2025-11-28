import pandas as pd   
import matplotlib.pyplot as plt  
import random

def searchPlayerStats(playerName): 

    dataSet = pd.read_csv("nbaNew.csv") 
    
    dataSet["PlayerName"] = dataSet["PlayerName"].str.replace("*", "")
    d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()   

    d["PPG"] = d["PTS"]/d["G"]  
    d["RPG"] = d["TRB"]/d["G"]  
    d["APG"] = d["AST"]/d["G"]  
    ppg = d.loc[playerName]["PPG"] 
    rbg = d.loc[playerName]["RPG"] 
    apg = d.loc[playerName]["APG"] 


    print(d.loc[playerName][["PPG", "RPG", "APG"]]) 
    print(f"{playerName} has played for the following") 
    teamQuery = dataSet[dataSet["PlayerName"] == playerName]  
    print(teamQuery[["Tm"]].drop_duplicates())   

    yearQuery = dataSet[dataSet["PlayerName"] == playerName]  
    rookieYear = yearQuery["SeasonStart"].min() 
    finalYear = yearQuery["SeasonStart"].max() 
    yearsPlayed = yearQuery["SeasonStart"].count()   

    plt.title(playerName)
    plt.bar(["PPG", "RPG", "APG"], [ppg, rbg, apg], color = ["red", "black", "orange"])  

    print(f"{playerName} was in the NBA for a total of {yearsPlayed} years from {rookieYear} to {finalYear}")
    
    plt.show()
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

def compareTwoPlayers(player1, player2):  

    dataSet = pd.read_csv("nbaNew.csv")
    dataSet["PlayerName"] = dataSet["PlayerName"].str.replace("*", "")
    d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()   

    d["PPG"] = d["PTS"]/d["G"]  
    d["RPG"] = d["TRB"]/d["G"]  
    d["APG"] = d["AST"]/d["G"]  

    p1points = d.loc[player1]["PPG"] 
    p2points = d.loc[player2]["PPG"]   

    p1Reb = d.loc[player1]["RPG"]  
    p2Reb = d.loc[player2]["RPG"]  

    p1Asg = d.loc[player1]["APG"] 
    p2Asg = d.loc[player2]["APG"] 

    


    p = [p1points, p2points]
    print(player1)
    print(d.loc[player1][["PPG", "RPG", "APG"]]) 

    print(player2) 
    print(d.loc[player2][["PPG", "RPG", "APG"]]) 


    figure, axis = plt.subplots(1, 3)   


    axis[0].bar([player1, player2], [p1points, p2points], color = ["green", "blue"]) 
    axis[0].set_title("Points Per Game") 

    axis[1].bar([player1, player2], [p1Reb, p2Reb], color = ["green", "blue"]) 
    axis[1].set_title("Rebounds Per Game") 

    axis[2].bar([player1, player2], [p1Asg, p2Asg], color = ["green", "blue"]) 
    axis[2].set_title("Assists Per Game")

    plt.show() 


def compareThreePlayers(player1, player2, player3): 
    dataSet = pd.read_csv("nbaNew.csv")
    dataSet["PlayerName"] = dataSet["PlayerName"].str.replace("*", "")
    d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()   

    d["PPG"] = d["PTS"]/d["G"]  
    d["RPG"] = d["TRB"]/d["G"]  
    d["APG"] = d["AST"]/d["G"]  

    p1points = d.loc[player1]["PPG"] 
    p2points = d.loc[player2]["PPG"] 
    p3points = d.loc[player3]["PPG"]

    p1Reb = d.loc[player1]["RPG"]  
    p2Reb = d.loc[player2]["RPG"]
    p3Reb = d.loc[player3]["RPG"]


    p1Asg = d.loc[player1]["APG"] 
    p2Asg = d.loc[player2]["APG"]  
    p3Asg = d.loc[player3]["APG"]  

    p = [p1points, p2points, p3points]
    print(player1)
    print(d.loc[player1][["PPG", "RPG", "APG"]]) 

    print(player2) 
    print(d.loc[player2][["PPG", "RPG", "APG"]])  

    print(player3)
    print(d.loc[[player3]][["PPG", "RPG", "APG"]])

    figure, axis = plt.subplots(1, 3)   

    axis[0].bar([player1, player2, player3], [p1points, p2points, p3points], color = ["green", "blue", "red"]) 
    axis[0].set_title("Points Per Game")  

    axis[1].bar([player1, player2, player3], [p1Reb, p2Reb, p3Reb], color = ["green", "blue", "red"]) 
    axis[1].set_title("Rebounds Per Game")

    axis[2].bar([player1, player2, player3], [p1Asg, p2Asg, p3Asg], color = ["green", "blue", "red"]) 
    axis[2].set_title("Assists Per Game") 


    plt.show() 

def playerVsplayer():  
    #create visual suplots for this one as well 
    #needs minor fixes to reveal names after but functionality works 
    num1 = random.randint(1,3920) 
    num2 = random.randint(1,3920) 
    
    dataSet = pd.read_csv("nbaNew.csv")
    dataSet["PlayerName"] = dataSet["PlayerName"].str.replace("*", "")
    d = dataSet.groupby("PlayerName")[["PTS", "G", "AST", "TRB"]].sum()     

    d["PPG"] = d["PTS"]/d["G"]  
    d["RPG"] = d["TRB"]/d["G"]  
    d["APG"] = d["AST"]/d["G"] 
    
    print("Player A")
    print(d.iloc[num1][["PPG", "RPG", "APG"]])
    print()  
    print("Player B")
    print(d.iloc[num2][["PPG", "RPG", "APG"]]) 
    return None 

def compareMinsToRest(player):  
    nbaGameMins = 48 
    dataSet = pd.read_csv("nbaNew.csv")
    dataSet["PlayerName"] = dataSet["PlayerName"].str.replace("*", "") 
    d = dataSet.groupby("PlayerName")[["MP", "G"]].sum() 
    d["MPG"] = d["MP"]/d["G"] 

    mpg = d.loc[player]["MPG"] 
    print(f"{player} minutes per game is {mpg}")
    nbaGameMins -= mpg
    plt.pie([mpg, nbaGameMins], labels=["Player Minutes", "Rest"])  
    plt.title(f"{player} mins vs rest") 
    plt.legend(["Minutes Per Game", "Rest"])
    plt.show() 


def playerHistory(player):
   dataSet = pd.read_csv("nbaNew.csv")  
   dataSet["PlayerName"] = dataSet["PlayerName"].str.replace("*", "") 

   

   dataSet = dataSet[dataSet["PlayerName"] == player] 

   dataSet["PPG"] = dataSet["PTS"]/dataSet["G"] 
   dataSet["RPG"] = dataSet["TRB"]/dataSet["G"] 
   dataSet["APG"] = dataSet["AST"]/dataSet["G"] 
   dataSet["MPG"] = dataSet["MP"]/dataSet["G"] 
    
   print(dataSet[["SeasonStart", "PPG", "RPG", "APG", "MPG"]].to_string()) 

   

   X = dataSet["SeasonStart"] #years 
   Y = dataSet["PPG"] 
   Y2 = dataSet["RPG"] 
   Y3 = dataSet["APG"] 
   Y4 = dataSet["MPG"]

   figure, axis = plt.subplots(2,2)
   
   axis[0, 0].fill_between(X, Y, color = "green")
   axis[0, 0].plot(X, Y)   
#    plt.setp(axis, xticks = X)
   axis[0, 0].set_title("Points Per Game")
   
   axis[0, 1].fill_between(X, Y2, color = "orange")
   axis[0, 1].plot(X, Y2, color = "yellow")
   axis[0, 1].set_title("Rebounds Per Game")

   axis[1, 0].fill_between(X, Y3, color = "pink")
   axis[1, 0].plot(X, Y3, color = "purple") 
   axis[1, 0].set_title("Assists Per Game") 
   
   axis[1, 1].fill_between(X, Y4, color = "purple")
   axis[1, 1].plot(X, Y4, color = "pink") 
   axis[1, 1].set_title("Minutes Per Game") 

   plt.show()


def FiveOnFive():  
    df = pd.read_csv("nbaNew.csv") 
    df["PlayerName"] = df["PlayerName"].str.replace("*", "") 
    team1 = [] 
    team2 = [] 
    points1 = [] 
    points2 = [] 

    while len(team1) < 5 or len(team2) < 5:  
        chosenPlayerTeam1 = str(input("Enter Player Name: (Team 1): ")) 
        team1.append(chosenPlayerTeam1) 
        chosenPlayerTeam2 = str(input("Enter Player Name (Team 2): ")) 
        team2.append(chosenPlayerTeam2) 
    

    d = df.groupby("PlayerName")[["PTS", "G"]].sum()
    d["PPG"] = d["PTS"]/d["G"] 

    for player in team1: 
        res = d.loc[player]["PPG"]
        points1.append(res) 
    for player in team2: 
         res = d.loc[player]["PPG"]
         points2.append(res) 

    totalPoints1 = sum(points1) 
    totalPoints1 = round(totalPoints1) 
    
    totalPoints2 = sum(points2) 
    totalPoints2 = round(totalPoints2)

    if totalPoints1 > totalPoints2: 
        print(f"Team 1 wins with your final score of {totalPoints1} - {totalPoints2}")
        plt.bar(["Team 1", "Team 2"], [totalPoints1, totalPoints2], color = ["orange", "purple"])
        plt.title("Five on Five result") 
        plt.show()

 
    print(f"Team 2 wins with your final score of {totalPoints1} - {totalPoints2}")
    plt.title("Five on Five result")
    # plt.bar(["Team 1", "Team 2"], [totalPoints1, totalPoints2], color = ["orange", "purple"])

    plt.show() 




def showDraftClass(draftClass):  

    df = pd.read_csv("nbaNew.csv") 
    df = df.groupby("PlayerName")[["SeasonStart"]].min() 
    df = df[df["SeasonStart"] == draftClass]
    

    print(df.to_string())
      

def main(): 
    print("Wlecome to NBA Finder: ") 
    running = True
    while running: 
        choice = int(input("Choose an option: \n (1) Search Player Stats \n (2) Search Top 5 players in CSV \n (3) Find Worst 5 in CSV \n (4) Compare Two Players \n (5) Compare Three Players \n (6) Player A vs Player B Comparison \n (7) Track Player Mins vs Rest \n (8) Track Player History \n (9) 5 on 5 Draft \n (0) Exit: \n (11) Find Draft Class ")) 
        if choice == 0: 
            running = False  
        elif choice == 1:  
            player = str(input("Enter Player Name: ")) 
            searchPlayerStats(player) 
        elif choice == 2: 
            findTopFive() 
        elif choice == 3: 
            findWorstFive() 
        elif choice == 4: 
            p1 = str(input("Enter Player 1: ")) 
            p2 = str(input("Enter Player 2: ")) 
            compareTwoPlayers(p1, p2) 
        elif choice == 5:
            p1 = str(input("Enter Player 1: ")) 
            p2 = str(input("Enter Player 2: "))  
            p3 = str(input("Enter Player 3: "))
            compareThreePlayers(p1, p2, p3) 
        elif choice == 6: 
            playerVsplayer()  
        elif choice == 7: 
            player = str(input("Enter Player Name: ")) 
            compareMinsToRest(player) 
        elif choice == 8:
            player = str(input("Enter Player Name: ")) 
            playerHistory(player) 
        elif choice == 9: 
            FiveOnFive()  
        elif choice == 11: 
            dc = int(input("Enter Draft class: ")) 
            showDraftClass(dc)

main() 









