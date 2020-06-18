import math
import random
import csv
import pandas as pd

def GetAllHands():
    """This function generates all hands possible
    in terms of reduced trump form (RTF) and writes them
    to AllHands.txt. """
    
    cards = ["RJT","LJT","AT","KT","QT","TT","NT",
    "ASS","KSS","QSS","TSS","NSS",
    "AOS1","KOS1","QOS1","JOS1","TOS1","NOS1",
    "AOS2","KOS2","QOS2","JOS2","TOS2","NOS2",]

    f = open("AllHands.txt","w")

    for j in range(0,20): 
        for k in range(1,21):
            if k != j and k > j:
                for l in range (2,22):
                    if l != j and l != k and l > k:
                        for m in range(3,23):
                            if m != l and m != k and m != j and m > l:
                                for n in range(4,24):
                                    if n != m and n != l and n != k and n != j and n > m:
                                        f.write("{},{},{},{},{}\n".format(cards[j],cards[k],cards[l],cards[m],cards[n]))
    f.close()   

    return None

def GetAllScenarios():
    """This function generates all hands possible
    in terms of reduced trump form (RTF) and writes them
    to OrderUpData folder and correct file"""
    
    topcardoptions = [0,2,3,4,5,6]
    printstring = []

    for i in range(4): #position
        for o in range(0,6): #Topcard
            for j in range(0,20): 
                if j != topcardoptions[o]:
                    for k in range(1,21):
                        if k != j and k > j and k != topcardoptions[o]:
                            for l in range (2,22):
                                if l != j and l != k and l > k and l != topcardoptions[o]:
                                    for m in range(3,23):
                                        if m != l and m != k and m != j and m > l and m != topcardoptions[o]:
                                            for n in range(4,24):
                                                if n != m and n != l and n != k and n != j and n > m and n != topcardoptions[o]:
                                                    printstring.append("{},{},{},{},{},{},{}\n".format(i,topcardoptions[o],j,k,l,m,n)) 
                                                    #Key:
                                                    #Pos,Topcard,Card1,Card2,Card3,Card4,Card5,TimesEuched,TimesGotMajority,TimesGotAll5
            #f = open("LonerOrderUpData/{}_{}.txt".format(i,topcardoptions[o]),"w") 
            #for _ in range(len(printstring)):
            #    f.write(printstring[0])
            #    printstring.pop(0)
            #print("Successfully populated {}_{}".format(i,topcardoptions[o]))
    f = open("AllScenarios.txt","w")
    for i in range(len(printstring)):
        f.write(printstring[i])
    print('{} possible scenarios'.format(len(printstring)))
    f.close()   

    return None

def PlayerData():
    """Takes in all games played and returns array in format
    Player Name, Wins, Losses, GP, Average Points, Teammate Win %, Teammate GP, Opponent Win %, Opponent GP, Avg Differential
    """

    playernamepos = [0,2,6,8]
    players = []
    playernames = []

    with open("GameLog.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        games = list(csvreader)
        for i in range(len(games)):
            games[i] = list(games[i])
    #games[0][0] = games[0][0][3:] #Removing ï»¿ (encoding error) [Update to VSCode fixed this]

    for i in range(len(games)):
        for j in range(4):
            if [games[i][playernamepos[j]]] not in players:
                players.append([games[i][playernamepos[j]]])
                playernames.append(games[i][playernamepos[j]])
                
    for i in range(len(players)):
        for _ in range(9):
            players[i].append(0) #Wins, Losses, GP, Average Points, Teammate Win %, Teammate GP, Opponent Win %, Opponent GP, Average Differential
    
    for i in range(len(games)): 
        for j in range(4):
            players[playernames.index(games[i][playernamepos[j]])][3] = players[playernames.index(games[i][playernamepos[j]])][3] + 1  #Total Games Played
        if int(games[i][4]) >= 10: #Team 1 Wins
            for j in range(2):
                players[playernames.index(games[i][playernamepos[j]])][1] = players[playernames.index(games[i][playernamepos[j]])][1] + 1 #Team1 Wins
            for k in range(2):
                players[playernames.index(games[i][playernamepos[k+2]])][2] = players[playernames.index(games[i][playernamepos[k+2]])][2] + 1 #Team2 Loses
        else: #Team 2 Wins
            for j in range(2):
                players[playernames.index(games[i][playernamepos[j]])][2] = players[playernames.index(games[i][playernamepos[j]])][2] + 1 #Team1 Loses
            for k in range(2):
                players[playernames.index(games[i][playernamepos[k+2]])][1] = players[playernames.index(games[i][playernamepos[k+2]])][1] + 1 #Team2 Wins
        for j in range(4): #Average Points/Differential
            if j < 2: #Team 1
                players[playernames.index(games[i][playernamepos[j]])][4] = round((players[playernames.index(games[i][playernamepos[j]])][4] * (players[playernames.index(games[i][playernamepos[j]])][3] - 1) + int(games[i][4])) /  players[playernames.index(games[i][playernamepos[j]])][3],1)
                players[playernames.index(games[i][playernamepos[j]])][9] = round((players[playernames.index(games[i][playernamepos[j]])][9] * (players[playernames.index(games[i][playernamepos[j]])][3] - 1) + (int(games[i][4]) - int(games[i][5]))) /  players[playernames.index(games[i][playernamepos[j]])][3],1)
            else:
                players[playernames.index(games[i][playernamepos[j]])][4] = round((players[playernames.index(games[i][playernamepos[j]])][4] * (players[playernames.index(games[i][playernamepos[j]])][3] - 1) + int(games[i][5])) /  players[playernames.index(games[i][playernamepos[j]])][3],1)
                players[playernames.index(games[i][playernamepos[j]])][9] = round((players[playernames.index(games[i][playernamepos[j]])][9] * (players[playernames.index(games[i][playernamepos[j]])][3] - 1) + (int(games[i][5]) - int(games[i][4]))) /  players[playernames.index(games[i][playernamepos[j]])][3],1)
        #Teammate win section:
        players[playernames.index(games[i][0])][5] = round(((players[playernames.index(games[i][0])][5] * players[playernames.index(games[i][0])][6]) + players[playernames.index(games[i][2])][1])/(players[playernames.index(games[i][0])][6] + players[playernames.index(games[i][2])][3]),3)
        players[playernames.index(games[i][2])][5] = round(((players[playernames.index(games[i][2])][5] * players[playernames.index(games[i][2])][6]) + players[playernames.index(games[i][0])][1])/(players[playernames.index(games[i][2])][6] + players[playernames.index(games[i][0])][3]),3)                      
        players[playernames.index(games[i][6])][5] = round(((players[playernames.index(games[i][6])][5] * players[playernames.index(games[i][6])][6]) + players[playernames.index(games[i][8])][1])/(players[playernames.index(games[i][6])][6] + players[playernames.index(games[i][8])][3]),3)
        players[playernames.index(games[i][8])][5] = round(((players[playernames.index(games[i][8])][5] * players[playernames.index(games[i][8])][6]) + players[playernames.index(games[i][6])][1])/(players[playernames.index(games[i][8])][6] + players[playernames.index(games[i][6])][3]),3)
        players[playernames.index(games[i][0])][6] = players[playernames.index(games[i][0])][6] + players[playernames.index(games[i][2])][3]
        players[playernames.index(games[i][2])][6] = players[playernames.index(games[i][2])][6] + players[playernames.index(games[i][0])][3]
        players[playernames.index(games[i][6])][6] = players[playernames.index(games[i][6])][6] + players[playernames.index(games[i][8])][3]
        players[playernames.index(games[i][8])][6] = players[playernames.index(games[i][8])][6] + players[playernames.index(games[i][6])][3]
        #Opponent win section:
        players[playernames.index(games[i][0])][7] = round((players[playernames.index(games[i][0])][8] * players[playernames.index(games[i][0])][7] + players[playernames.index(games[i][6])][1] + players[playernames.index(games[i][8])][1])/(players[playernames.index(games[i][0])][8] + players[playernames.index(games[i][6])][3] + players[playernames.index(games[i][8])][3]),3) 
        players[playernames.index(games[i][2])][7] = round((players[playernames.index(games[i][2])][8] * players[playernames.index(games[i][2])][7] + players[playernames.index(games[i][6])][1] + players[playernames.index(games[i][8])][1])/(players[playernames.index(games[i][2])][8] + players[playernames.index(games[i][6])][3] + players[playernames.index(games[i][8])][3]),3) 
        players[playernames.index(games[i][6])][7] = round((players[playernames.index(games[i][6])][8] * players[playernames.index(games[i][6])][7] + players[playernames.index(games[i][0])][1] + players[playernames.index(games[i][2])][1])/(players[playernames.index(games[i][6])][8] + players[playernames.index(games[i][0])][3] + players[playernames.index(games[i][2])][3]),3) 
        players[playernames.index(games[i][8])][7] = round((players[playernames.index(games[i][8])][8] * players[playernames.index(games[i][8])][7] + players[playernames.index(games[i][0])][1] + players[playernames.index(games[i][2])][1])/(players[playernames.index(games[i][8])][8] + players[playernames.index(games[i][0])][3] + players[playernames.index(games[i][2])][3]),3) 
        players[playernames.index(games[i][0])][8] = players[playernames.index(games[i][0])][8] + players[playernames.index(games[i][6])][3] + players[playernames.index(games[i][8])][3]
        players[playernames.index(games[i][2])][8] = players[playernames.index(games[i][2])][8] + players[playernames.index(games[i][6])][3] + players[playernames.index(games[i][8])][3]
        players[playernames.index(games[i][6])][8] = players[playernames.index(games[i][6])][8] + players[playernames.index(games[i][0])][3] + players[playernames.index(games[i][2])][3]
        players[playernames.index(games[i][8])][8] = players[playernames.index(games[i][8])][8] + players[playernames.index(games[i][0])][3] + players[playernames.index(games[i][2])][3]
        
    return players

def RankPlayers(players):
    """
    Reads in [Player Name, Wins, Losses, GP, Average Points, Teammate Win %, Teammate GP, Opponent Win %, Opponent GP, Avg Differential]
    and Ranks players according to criteria set forth
    """
    #Weights:
    WIN_PER = 10
    AVG_PTS = 4 
    AVG_DIFF = 1
    TM_WIN_PER = -3
    GP = -1
    OPP_WIN_PER = 3 
    ranks = []
    initorder = []

    for i in range(len(players)): #Creating Rank List
        ranks.append([players[i][0]])
        initorder.append(players[i][0])
        players[i][6] = players[i][6] / players[i][3] #Average teammate gp 
        players[i][8] = players[i][8] / players[i][3] #average opp gp
        for _ in range(10): #win %, GP rank, avgPts %, team win %, Teammate GP Rank, opp win %, Opp GP Rank, Wins, Losses, Avg Diff
            ranks[i].append(0)
        #Easy transfer Data
        ranks[i][1] = round(players[i][1]/players[i][3],3)
        ranks[i][3] = round(players[i][4]/10,3)
        ranks[i][4] = players[i][5]
        ranks[i][6] = players[i][7]
        ranks[i][8] = players[i][1]
        ranks[i][9] = players[i][2]
        ranks[i][10] = players[i][9]/10 #Dividing by 10 to get a good multiplier

    #GP rank normalized
    players.sort(key=lambda x: x[3], reverse=True) #descending order as to create negative percentile
    for i in range(len(players)):
        ranks[initorder.index(players[i][0])][2] = round(1/(players[i][3]/players[0][3]),2)
        if players[i][3] < 5: #Not enough samples
            ranks[initorder.index(players[i][0])].append(10)
        elif players[i][3] < 10: #Still not enough samples
            ranks[initorder.index(players[i][0])].append(4)
        else: #Enough games played
            ranks[initorder.index(players[i][0])].append(0)

    #Teammate GP rank normalized
    players.sort(key=lambda x: x[6]) 
    for i in range(len(players)):
        ranks[initorder.index(players[i][0])][5] = round((i+1)/len(players),2)

    #opp GP rank normalized
    players.sort(key=lambda x: x[8]) #ascending order as to create positive precentile
    for i in range(len(players)):
        ranks[initorder.index(players[i][0])][7] = round((i+1)/len(players),2)
    
    for i in range(len(ranks)):
        rawscore = ranks[i][1] * WIN_PER + ranks[i][11] * GP + ranks[i][3] * AVG_PTS + ranks[i][4] * TM_WIN_PER + ranks[i][6] * OPP_WIN_PER + ranks[i][10] * AVG_DIFF
        ranks[i].append(rawscore)
        #THEORETICAL MAX SCORE: 19.5
        ranks[i][1] = ranks[i][1] * 100 #Adjusting to readable format
        ranks[i][4] = ranks[i][4] * 100
        ranks[i][6] = ranks[i][6] * 100
        ranks[i][3] = ranks[i][3] * 10
        ranks[i][10] = ranks[i][10] * 10
        ranks[i][2] = len(ranks) - int(round(ranks[i][2] * len(ranks),0)) 
        ranks[i][5] = len(ranks) - int(round(ranks[i][5] * len(ranks),0)) + 1
        ranks[i][7] = len(ranks) - int(round(ranks[i][7] * len(ranks),0)) + 1

    ranks.sort(key=lambda x: x[2],reverse=True) #Fixing GP Rank
    for i in range(len(ranks)):
        ranks[i][2] = i + 1

    #Final Ranking
    ranks.sort(key=lambda x: x[12],reverse=True) 
    data={'Name':[i[0] for i in ranks], 'WINS':[i[8] for i in ranks], 'LOSSES':[i[9] for i in ranks],
    'WIN %': [i[1] for i in ranks],'GP Rank':[i[2] for i in ranks],
    "AVG PTS":[i[3] for i in ranks],"AVG DIFF":[i[10] for i in ranks],
    "AVG TM WIN %":[i[4] for i in ranks],"AVG TM GP Rank":[i[5] for i in ranks],"AVG OPP WIN %":[i[6] for i in ranks],"AVG OPP GP Rank":[i[7] for i in ranks],
    "Ranking Score":[i[12] for i in ranks]}
    #Note: Rankings of GP, TM GP, and OPP GM: 1 means most games played, last means least games played
    result=pd.DataFrame(data=data)
    result=round(result,4)
    result.index += 1
    print(result) 

    result = result.drop(["WIN %", "GP Rank", "AVG TM GP Rank", "AVG OPP GP Rank", "Ranking Score"], axis=1)
    result.to_csv("Standings/IndividualRankings.csv")

    return None

def SeeHead2Head(player1,player2,showResults):
    """Want to compare two players to eachother?
    This returns a few stats about all their common games"""
    players = []
    playernames = []
    statsSame = [0,0,0,0] #W, L, Avg Pts, Avg Differential
    statsOpp = [0,0,0,0] #P1 W, P2 W, Avg P1 Pts, Avg P2 Pts
    comGamesSame = [] #Storing all common games
    comGamesOpp = []
    playernamepos = [0,2,6,8]

    with open("GameLog.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        games = list(csvreader)
        for i in range(len(games)):
            games[i] = list(games[i])
    games[0][0] = games[0][0][3:] #Removing ï»¿ (encoding error)

    for i in range(len(games)):
        for j in range(4):
            if [games[i][playernamepos[j]]] not in players:
                players.append([games[i][playernamepos[j]]])
                playernames.append(games[i][playernamepos[j]])
    
    if player1 not in playernames:
        raise Exception("Name \"{}\" not found in Game Log, check spelling".format(player1))
    elif player2 not in playernames:
        raise Exception("Name \"{}\" not found in Game Log, check spelling".format(player2))

    for i in range(len(games)):
        if player1 == games[i][0] and player2 == games[i][2] or player1 == games[i][6] and player2 == games[i][8] or player2 == games[i][0] and player1 == games[i][2] or player2 == games[i][6] and player1 == games[i][8]:
            comGamesSame.append(i)
        elif ((player1 == games[i][0] or player1 == games[i][2]) and (player2 == games[i][6] or player2 == games[i][8])) or ((player2 == games[i][0] or player2 == games[i][2]) and (player1 == games[i][6] or player1 == games[i][8])):
            comGamesOpp.append(i)

    for i in range(len(comGamesSame)): #Same games
        if player1 == games[comGamesSame[i]][0] or player1 == games[comGamesSame[i]][2]: #Team 1
            if int(games[comGamesSame[i]][4]) > int(games[comGamesSame[i]][5]): #Won
                statsSame[0] = statsSame[0] + 1
            else: 
                statsSame[1] = statsSame[1] + 1
            statsSame[2] = round((statsSame[2] * (statsSame[0] + statsSame[1] - 1) + int(games[comGamesSame[i]][4]))/(statsSame[0] + statsSame[1]),1) #Avg pts
            statsSame[3] = round((statsSame[3] * (statsSame[0] + statsSame[1] - 1) + int(games[comGamesSame[i]][4]) - int(games[comGamesSame[i]][5]))/(statsSame[0] + statsSame[1]),1) #Avg diff
        else: #Team 2
            if int(games[comGamesSame[i]][5]) > int(games[comGamesSame[i]][4]):
                statsSame[0] = statsSame[0] + 1
            else: 
                statsSame[1] = statsSame[1] + 1 
            statsSame[2] = round((statsSame[2] * (statsSame[0] + statsSame[1] - 1) + int(games[comGamesSame[i]][5]))/(statsSame[0] + statsSame[1]),1) #Avg pts
            statsSame[3] = round((statsSame[3] * (statsSame[0] + statsSame[1] - 1) + int(games[comGamesSame[i]][5]) - int(games[comGamesSame[i]][4]))/(statsSame[0] + statsSame[1]),1) #Avg diff

    for i in range(len(comGamesOpp)): #Head to head
        if player1 == games[comGamesOpp[i]][0] or player1 == games[comGamesOpp[i]][2]: # Player 1 on Team 1 
            if int(games[comGamesOpp[i]][4]) > int(games[comGamesOpp[i]][5]): #Player1 won
                statsOpp[0] = statsOpp[0] + 1
            else:
                statsOpp[1] = statsOpp[1] + 1
            statsOpp[2] = round((statsOpp[2] * (statsOpp[0] + statsOpp[1] - 1) + int(games[comGamesOpp[i]][4]))/(statsOpp[0] + statsOpp[1]),1) #Avg pts P1
            statsOpp[3] = round((statsOpp[3] * (statsOpp[0] + statsOpp[1] - 1) + int(games[comGamesOpp[i]][5]))/(statsOpp[0] + statsOpp[1]),1) #Avg pts P2
        else: #Player 2 on team 1
            if int(games[comGamesOpp[i]][4]) > int(games[comGamesOpp[i]][5]): #Player2 won
                statsOpp[1] = statsOpp[1] + 1
            else:
                statsOpp[0] = statsOpp[0] + 1
            statsOpp[2] = round((statsOpp[2] * (statsOpp[0] + statsOpp[1] - 1) + int(games[comGamesOpp[i]][5]))/(statsOpp[0] + statsOpp[1]),1) #Avg pts P1
            statsOpp[3] = round((statsOpp[3] * (statsOpp[0] + statsOpp[1] - 1) + int(games[comGamesOpp[i]][4]))/(statsOpp[0] + statsOpp[1]),1) #Avg pts P2
    
    if showResults == True:
        print("\n{} and {} have been on the same team {} times.".format(player1,player2,(statsSame[0] + statsSame[1]))) #On the same team
        if (statsSame[0] + statsSame[1]) != 0:
            print("In these games, they have:\n{} W, {} L ({}% Win Rate)\nWith an average of {} pts/game and a {} points difference/game".format(statsSame[0],statsSame[1],round((statsSame[0]/(statsSame[0]+statsSame[1]) * 100),1),statsSame[2],statsSame[3]))
        print("\n{} and {} have played each other {} times.".format(player1,player2,(statsOpp[0] + statsOpp[1]))) #On opposite team
        if (statsOpp[0] + statsOpp[1]) != 0:
            print("In these games:\n{} has {} wins and {} has {} wins".format(player1,statsOpp[0],player2,statsOpp[1]))
            print("{} is averaging {} pts/game and {} is averaging {} pts/game\n".format(player1,statsOpp[2],player2,statsOpp[3])) 
        return None
    else: #For determining rivalries
        returnlist = []
        for i in range(4):
            returnlist.append(statsSame[i])
        for i in range(4):
            returnlist.append(statsOpp[i])
        return returnlist

def Rivalries(testplayer,showResults):
    """Calculates head to head for all players in relation to one player
    returns best/worst rivalries"""
    playernamepos = [0,2,6,8]
    players = []
    #TEAMMATE LISTS
    bestteammatew = [0,0] #[Name,Win%]
    worstteammatel = [0,100] #[Name,Win%]
    mostcommonteam = [0,0,0] #[Name,W,L]
    mostwinswith = [0,0]
    mostLswith = [0,0]
    bestppg = [0,0]
    worstppg = [0,13]
    #OPP LISTS
    mostcommonopp = [0,0,0]
    mostwinsagainst = [0,0]
    mostLsto = [0,0]
    bestwinper = [0,0]
    worstwinper = [0,100]
    bestppgag = [0,0]
    worstppgag = [0,13]

    with open("GameLog.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        games = list(csvreader)
        for i in range(len(games)):
            games[i] = list(games[i])
    games[0][0] = games[0][0][3:] #Removing ï»¿ (encoding error)

    for i in range(len(games)):
        for j in range(4):
            if [games[i][playernamepos[j]]] not in players:
                players.append([games[i][playernamepos[j]]])
             
    for i in range(len(players)):
        if players.index([testplayer]) != i:
            players[i].append(SeeHead2Head(testplayer,players[i][0], False))
    
    for i in range(len(players)):
        if players.index([testplayer]) != i:
            if players[i][1] == [0,0,0,0,0,0,0,0]:
                pass #No overlap, disregard to speed up process
            else: #Have played with/against
                if players[i][1][0] + players[i][1][1] != 0: #Have played with
                    if players[i][1][0] > mostwinswith[1]: 
                        mostwinswith[0] = players[i][0]
                        mostwinswith[1] = players[i][1][0]
                    if players[i][1][1] > mostLswith[1]: 
                        mostLswith[0] = players[i][0]
                        mostLswith[1] = players[i][1][1]
                    if players[i][1][0] + players[i][1][1] > mostcommonteam[1] + mostcommonteam[2]:
                        mostcommonteam[0] =  players[i][0]
                        mostcommonteam[1] =  players[i][1][0]
                        mostcommonteam[2] =  players[i][1][1]
                    if players[i][1][0]/(players[i][1][0] + players[i][1][1])*100 > bestteammatew[1]:
                        bestteammatew[0] =  players[i][0]
                        bestteammatew[1] =  round(players[i][1][0]/(players[i][1][0] + players[i][1][1])*100,1)
                    if players[i][1][0]/(players[i][1][0] + players[i][1][1])*100 < worstteammatel[1]:
                        worstteammatel[0] =  players[i][0]
                        worstteammatel[1] =  round(players[i][1][0]/(players[i][1][0] + players[i][1][1])*100,1)
                    if players[i][1][2] > bestppg[1]:
                        bestppg[0] = players[i][0]
                        bestppg[1] = players[i][1][2]
                    if players[i][1][2] < worstppg[1]:
                        worstppg[0] = players[i][0]
                        worstppg[1] = players[i][1][2]

                if players[i][1][4] + players[i][1][5] != 0: #Have played against
                    if players[i][1][4] > mostwinsagainst[1]: 
                        mostwinsagainst[0] = players[i][0]
                        mostwinsagainst[1] = players[i][1][4]
                    if players[i][1][5] > mostLsto[1]: 
                        mostLsto[0] = players[i][0]
                        mostLsto[1] = players[i][1][5]
                    if players[i][1][4] + players[i][1][5] > mostcommonopp[1] + mostcommonopp[2]:
                        mostcommonopp[0] =  players[i][0]
                        mostcommonopp[1] =  players[i][1][4]
                        mostcommonopp[2] =  players[i][1][5]
                    if players[i][1][4]/(players[i][1][4] + players[i][1][5])*100 > bestwinper[1]:
                        bestwinper[0] =  players[i][0]
                        bestwinper[1] =  round(players[i][1][4]/(players[i][1][4] + players[i][1][5])*100,1)
                    if players[i][1][4]/(players[i][1][4] + players[i][1][5])*100 < worstwinper[1]:
                        worstwinper[0] =  players[i][0]
                        worstwinper[1] =  round(players[i][1][4]/(players[i][1][4] + players[i][1][5])*100,1)
                    if players[i][1][6] > bestppgag[1]:
                        bestppgag[0] = players[i][0]
                        bestppgag[1] = players[i][1][6]
                    if players[i][1][6] < worstppgag[1]:
                        worstppgag[0] = players[i][0]
                        worstppgag[1] = players[i][1][6]

    if showResults == True:
        print("\n{}".format(testplayer))
        print("\nTeammates:\nMost Common Teammate: {}, {} games, {} Wins, {} Losses ({}%)".format(mostcommonteam[0],mostcommonteam[1] + mostcommonteam[2],mostcommonteam[1],mostcommonteam[2],round((mostcommonteam[1]/(mostcommonteam[2]+mostcommonteam[1])*100),1)))
        print("Best Teammate (Win %):{}, {}%".format(bestteammatew[0],bestteammatew[1]))
        print("Worst Teammate (Win %):{}, {}%".format(worstteammatel[0],worstteammatel[1]))
        print("Most wins with:{}, {} wins".format(mostwinswith[0],mostwinswith[1]))
        print("Most losses with:{}, {} losses".format(mostLswith[0],mostLswith[1]))
        print("Best PPG with: {}, {} ppg".format(bestppg[0],bestppg[1]))
        print("Worst PPG with: {}, {} ppg\n".format(worstppg[0],worstppg[1]))

        print("Opponents:\nMost Common Opponent: {}, {} games, {} Wins, {} Losses ({}%)".format(mostcommonopp[0],mostcommonopp[1] + mostcommonopp[2],mostcommonopp[1],mostcommonopp[2],round((mostcommonopp[1]/(mostcommonopp[2]+mostcommonopp[1])*100),1)))
        print("Best Win % against:{}, {}%".format(bestwinper[0],bestwinper[1]))
        print("Worst Win % against:{}, {}%".format(worstwinper[0],worstwinper[1]))
        print("Most wins against:{}, {} wins".format(mostwinsagainst[0],mostwinsagainst[1]))
        print("Most losses against:{}, {} losses".format(mostLsto[0],mostLsto[1]))
        print("Best PPG against: {}, {} ppg".format(bestppgag[0],bestppgag[1]))
        print("Worst PPG against: {}, {} ppg\n".format(worstppgag[0],worstppgag[1]))

    else:
        pass


    return None

def LeagueStandings():
    """Reads in the individual rankings and outputs them to league csvs"""
    allrankings = pd.read_csv("Standings/IndividualRankings.csv")
    leagueaffil = pd.read_csv("Standings/leaguesrawdata.csv")
    rankings = []

    leaguedata = [[],[],[],[]]
    leaguedata[0] = leagueaffil["OKE"].to_list()
    leaguedata[1] = leagueaffil["TCC"].to_list()
    leaguedata[2] = leagueaffil["WSE"].to_list()
    leaguedata[3] = leagueaffil["ONE"].to_list()

    for i in range(len(allrankings)):
        rankings.append(allrankings["Name"].loc[i])
    
    for i in range(len(leaguedata)):
        leaguedata[i] = [j for j in leaguedata[i] if str(j) != 'nan']
    
    sorting = []
    for i in range(len(leaguedata)):
        for j in range(len(leaguedata[i])):
            sorting.append(rankings.index(leaguedata[i][j]))
        sorting = sorted(sorting)
        for k in range(len(leaguedata[i])):
            leaguedata[i][k] = rankings[sorting[0]]
            sorting.pop(0)
    #Leaguedata is now sorted in ascending order, time to print to csv
    for i in range(len(leaguedata)):
        f = open("Standings/league{}.csv".format(i+1), "w")
        for j in range(len(leaguedata[i])):
            f.write("{},{}\n".format(j+1,leaguedata[i][j]))
        f.close()

    return None

#Uncomment to Choose Which to Run:--------------------------------------------------------------------------
Players = PlayerData()
RankPlayers(Players)
#SeeHead2Head('Ben Gochanour','Nathan Woo',True)
#Rivalries("Nathan Woo",True)
#GetAllScenarios()
LeagueStandings()