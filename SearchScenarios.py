###This function sees the probablity of various outcomes based on a certain hand###
import pandas as pd
NEEDKEY = False
round1reg=pd.read_csv("Calling/Round1/Round1.csv")
round1lone=pd.read_csv("Calling/Round1/Round1_Loner.csv")
round2ss=pd.read_csv("Calling/Round2/Round2_ShortSuit.csv")
round2sslone=pd.read_csv("Calling/Round2/Round2_Lone_ShortSuit.csv")
round2os1=pd.read_csv("Calling/Round2/Round2_Offsuit1.csv")
round2os1lone=pd.read_csv("Calling/Round2/Round2_Lone_OffSuit1.csv")
round2os2=pd.read_csv("Calling/Round2/Round2_Offsuit2.csv")
round2os2lone=pd.read_csv("Calling/Round2/Round2_Lone_Offsuit2.csv")

def convert_to_analog():
    topcardraw = input("Input Top Card:")
    topcard = 0
    if topcardraw[0] == "J":
        topcard = 0
    elif topcardraw[0] == "A":
        topcard = 2
    elif topcardraw[0] == "K":
        topcard = 3
    elif topcardraw[0] == "Q":
        topcard = 4
    elif topcardraw[0] == "T":
        topcard = 5
    elif topcardraw[0] == "N":
        topcard = 6
    else:
        raise Exception("Invalid Top Card Value")
    cards = [0,0,0,0,0]
    for i in range(5):
        cards[i] = input("Card {}: ".format(i+1))
    for j in range(5):
        if cards[j][1] == topcardraw[1]: #in trump suit
            if cards[j][0] == "J":
                cards[j] = 0
            elif cards[j][0] == "A":
                cards[j] = 2
            elif cards[j][0] == "K":
                cards[j] = 3
            elif cards[j][0] == "Q":
                cards[j] = 4
            elif cards[j][0] == "T":
                cards[j] = 5
            elif cards[j][0] == "N":
                cards[j] = 6
        elif (topcardraw[1] == "H" and cards[j][1] == "D") or (topcardraw[1] == "D" and cards[j][1] == "H") or (topcardraw[1] == "C" and cards[j][1] == "S") or (topcardraw[1] == "S" and cards[j][1] == "C"): #in shortsuit
            if cards[j][0] == "J":
                cards[j] = 1
            elif cards[j][0] == "A":
                cards[j] = 7
            elif cards[j][0] == "K":
                cards[j] = 8
            elif cards[j][0] == "Q":
                cards[j] = 9
            elif cards[j][0] == "T":
                cards[j] = 10
            elif cards[j][0] == "N":
                cards[j] = 11
        elif (topcardraw[1] == "H" and cards[j][1] == "C") or (topcardraw[1] == "D" and cards[j][1] == "S") or (topcardraw[1] == "C" and cards[j][1] == "H") or (topcardraw[1] == "S" and cards[j][1] == "D"): #in os1
            if cards[j][0] == "J":
                cards[j] = 15
            elif cards[j][0] == "A":
                cards[j] = 12
            elif cards[j][0] == "K":
                cards[j] = 13
            elif cards[j][0] == "Q":
                cards[j] = 14
            elif cards[j][0] == "T":
                cards[j] = 16
            elif cards[j][0] == "N":
                cards[j] = 17
        elif (topcardraw[1] == "H" and cards[j][1] == "S") or (topcardraw[1] == "D" and cards[j][1] == "C") or (topcardraw[1] == "C" and cards[j][1] == "D") or (topcardraw[1] == "S" and cards[j][1] == "H"): #in os2
            if cards[j][0] == "J":
                cards[j] = 21
            elif cards[j][0] == "A":
                cards[j] = 18
            elif cards[j][0] == "K":
                cards[j] = 19
            elif cards[j][0] == "Q":
                cards[j] = 20
            elif cards[j][0] == "T":
                cards[j] = 22
            elif cards[j][0] == "N":
                cards[j] = 23
        else:
            raise Exception("Invalid Card Inputs")
    cards = sorted(cards)

    pos = input("Input Position (1 = Lead, 4 = Dealer):")
    pos = int(pos) - 1
    values = [pos]
    values.append(topcard)
    for i in range(5):
        values.append(cards[i])
    values.append(topcardraw) #for seeing what suit it was

    return values

def main():
    """Input top card, position, and hand, get stats"""
    if NEEDKEY == True:
        print("Guide to inputting cards:\n Type first letter of card value, then first letter of suit")
        print("Example: Ace of Hearts is inputted as \'AH\' (note capital letters, quotations not necessary).")
        print("For 9s and 10s, use N and T for the values, respectively.")
    
    print("\nSITUATION LOOKUP\nIf at any point you mis-input a card, press Ctrl+C to quit:\n\n")
    datastring = convert_to_analog()
    if datastring[7][1] == "C":
        ss = "Spades"
        os1 = "Hearts"
        os2 = "Diamonds"
    elif datastring[7][1] == "S":
        ss = "Clubs"
        os1 = "Diamonds"
        os2 = "Hearts"
    elif datastring[7][1] == "H":
        ss = "Hearts"
        os1 = "Clubs"
        os2 = "Spades"
    elif datastring[7][1] == "D":
        ss = "Hearts"
        os1 = "Spades"
        os2 = "Clubs"
    
    #ROUND 1 Lookups---------------------------------------------------------------------------------------
    Round1RegVal=round1reg.loc[(round1reg["Pos"]==datastring[0]) 
    & (round1reg["Top"]==datastring[1]) & (round1reg["C1"]==datastring[2])
    & (round1reg["C2"]==datastring[3]) & (round1reg["C3"]==datastring[4]) 
    & (round1reg["C4"]==datastring[5]) & (round1reg["C5"]==datastring[6])]['ExpectedPoints']
    Round1RegVal=Round1RegVal.reset_index(drop=True)
    Round1RegVal=float(Round1RegVal[0])
    
    Round1LoneVal=round1lone.loc[(round1lone["Pos"]==datastring[0]) & (round1lone["Top"]==datastring[1])
                 & (round1lone["C1"]==datastring[2])
                 & (round1lone["C2"]==datastring[3]) & (round1lone["C3"]==datastring[4]) 
                 & (round1lone["C4"]==datastring[5]) & (round1lone["C5"]==datastring[6])]['ExpectedPoints']
    Round1LoneVal=Round1LoneVal.reset_index(drop=True)
    Round1LoneVal=float(Round1LoneVal[0])

    #Round 2 Shortsuit Lookups-------------------------------------------------------------------------------
    Round2SSVal=round2ss.loc[(round2ss["Pos"]==datastring[0]) 
    & (round2ss["Top"]==datastring[1]) & (round2ss["C1"]==datastring[2])
    & (round2ss["C2"]==datastring[3]) & (round2ss["C3"]==datastring[4]) 
    & (round2ss["C4"]==datastring[5]) & (round2ss["C5"]==datastring[6])]['ExpectedPoints']
    Round2SSVal=Round2SSVal.reset_index(drop=True)
    Round2SSVal=float(Round2SSVal[0])
    
    Round2SSLoneVal=round2sslone.loc[(round1lone["Pos"]==datastring[0]) & (round2sslone["Top"]==datastring[1])
                 & (round2sslone["C1"]==datastring[2])
                 & (round2sslone["C2"]==datastring[3]) & (round2sslone["C3"]==datastring[4]) 
                 & (round2sslone["C4"]==datastring[5]) & (round2sslone["C5"]==datastring[6])]['ExpectedPoints']
    Round2SSLoneVal=Round2SSLoneVal.reset_index(drop=True)
    Round2SSLoneVal=float(Round2SSLoneVal[0])

    #Round 2 Offsuit1 Lookups-------------------------------------------------------------------------------
    Round2OS1Val=round2os1.loc[(round2os1["Pos"]==datastring[0]) 
    & (round2os1["Top"]==datastring[1]) & (round2os1["C1"]==datastring[2])
    & (round2os1["C2"]==datastring[3]) & (round2os1["C3"]==datastring[4]) 
    & (round2os1["C4"]==datastring[5]) & (round2os1["C5"]==datastring[6])]['ExpectedPoints']
    Round2OS1Val=Round2OS1Val.reset_index(drop=True)
    Round2OS1Val=float(Round2OS1Val[0])
    
    Round2OS1LoneVal=round2os1lone.loc[(round2os1lone["Pos"]==datastring[0]) & (round2os1lone["Top"]==datastring[1])
                 & (round2os1lone["C1"]==datastring[2])
                 & (round2os1lone["C2"]==datastring[3]) & (round2os1lone["C3"]==datastring[4]) 
                 & (round2os1lone["C4"]==datastring[5]) & (round2os1lone["C5"]==datastring[6])]['ExpectedPoints']
    Round2OS1LoneVal=Round2OS1LoneVal.reset_index(drop=True)
    Round2OS1LoneVal=float(Round2OS1LoneVal[0])

    #Round 2 Offsuit2 Lookups-------------------------------------------------------------------------------
    Round2OS2Val=round2os2.loc[(round2os2["Pos"]==datastring[0]) 
    & (round2os2["Top"]==datastring[1]) & (round2os2["C1"]==datastring[2])
    & (round2os2["C2"]==datastring[3]) & (round2os2["C3"]==datastring[4]) 
    & (round2os2["C4"]==datastring[5]) & (round2os2["C5"]==datastring[6])]['ExpectedPoints']
    Round2OS2Val=Round2OS2Val.reset_index(drop=True)
    Round2OS2Val=float(Round2OS2Val[0])
    
    Round2OS2LoneVal=round2os2lone.loc[(round1lone["Pos"]==datastring[0]) & (round2os2lone["Top"]==datastring[1])
                 & (round2os2lone["C1"]==datastring[2])
                 & (round2os2lone["C2"]==datastring[3]) & (round2os2lone["C3"]==datastring[4]) 
                 & (round2os2lone["C4"]==datastring[5]) & (round2os2lone["C5"]==datastring[6])]['ExpectedPoints']
    Round2OS2LoneVal=Round2OS2LoneVal.reset_index(drop=True)
    Round2OS2LoneVal=float(Round2OS2LoneVal[0])

    print("\nIf CALLED: Expected Points:{}".format(Round1RegVal))
    print("If CALLED ALONE: Expected Points:{}\n".format(Round1LoneVal))
    print("If {} Called: Expected Points:{}".format(ss,Round2SSVal))
    print("If {} Called ALONE: Expected Points:{}\n".format(ss,Round2SSLoneVal))
    print("If {} Called: Expected Points:{}".format(os1,Round2OS1Val))
    print("If {} Called ALONE: Expected Points:{}\n".format(os1,Round2OS1LoneVal))
    print("If {} Called: Expected Points:{}".format(os2,Round2OS2Val))
    print("If {} Called ALONE: Expected Points:{}\n".format(os2,Round2OS2LoneVal))

    return None

main()
