###This function sees the probablity of various outcomes based on a certain hand###
import pandas as pd
from tkinter import StringVar, Tk, N, W, E, S
from tkinter import ttk

round1reg=pd.read_csv("Round1.csv")
round1lone=pd.read_csv("Round1_Loner.csv")
round2ss=pd.read_csv("Round2_ShortSuit.csv")
round2sslone=pd.read_csv("Round2_Lone_ShortSuit.csv")
round2os1=pd.read_csv("Round2_Offsuit1.csv")
round2os1lone=pd.read_csv("Round2_Lone_OffSuit1.csv")
round2os2=pd.read_csv("Round2_Offsuit2.csv")
round2os2lone=pd.read_csv("Round2_Lone_Offsuit2.csv")

def calculate(*args):
    #Variable Declaration-------------------------
    topcardraw = topcardrawval.get()
    if topcardraw[0] == "J":
        topcard.set(0)
    elif topcardraw[0] == "A":
        topcard.set(2)
    elif topcardraw[0] == "K":
        topcard.set(3)
    elif topcardraw[0] == "Q":
        topcard.set(4)
    elif topcardraw[0] == "T":
        topcard.set(5)
    elif topcardraw[0] == "N":
        topcard.set(6)
    
    cards = [0,0,0,0,0]
    cards[0] = card1raw.get()
    cards[1] = card2raw.get()
    cards[2] = card3raw.get()
    cards[3] = card4raw.get()
    cards[4] = card5raw.get()

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

    cards = sorted(cards)
    card1.set(cards[0])
    card2.set(cards[1])
    card3.set(cards[2])
    card4.set(cards[3])
    card5.set(cards[4])

    pos = positionraw.get()
    pos = int(pos) - 1
    position.set(pos)

    datastring = []
    datastring.append(int(position.get()))
    datastring.append(int(topcard.get()))
    datastring.append(int(card1.get()))
    datastring.append(int(card2.get()))
    datastring.append(int(card3.get()))
    datastring.append(int(card4.get()))
    datastring.append(int(card5.get()))
    datastring.append(topcardraw)

    if datastring[7][1] == "C":
        ss = "Spades"
        os1 = "Hearts"
        os2 = "Diamonds"
    elif datastring[7][1] == "S":
        ss = "Clubs"
        os1 = "Diamonds"
        os2 = "Hearts"
    elif datastring[7][1] == "H":
        ss = "Diamonds"
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
    & (round1reg["C4"]==datastring[5]) & (round1reg["C5"]==datastring[6])]
    Round1RegVal=Round1RegVal.reset_index(drop=True)

    Round1RegE = Round1RegVal["PctEuched"]
    Round1RegM = Round1RegVal["PctMajority"]
    Round1Reg5 = Round1RegVal["PctAllFive"]
    Round1Pts = Round1RegVal["ExpectedPoints"]
    Round1Num = Round1RegVal["TotOverall"]
    
    Round1LoneVal=round1lone.loc[(round1lone["Pos"]==datastring[0]) & (round1lone["Top"]==datastring[1])
                 & (round1lone["C1"]==datastring[2])
                 & (round1lone["C2"]==datastring[3]) & (round1lone["C3"]==datastring[4]) 
                 & (round1lone["C4"]==datastring[5]) & (round1lone["C5"]==datastring[6])]
    Round1LoneVal=Round1LoneVal.reset_index(drop=True)
    Round1LoneE = Round1LoneVal["PctEuched"]
    Round1LoneM = Round1LoneVal["PctMajority"]
    Round1Lone5 = Round1LoneVal["PctAllFive"]
    Round1LonePts = Round1LoneVal["ExpectedPoints"]
    Round1LoneNum = Round1LoneVal["TotOverall"]

    #Round 2 Shortsuit Lookups-------------------------------------------------------------------------------
    Round2SSVal=round2ss.loc[(round2ss["Pos"]==datastring[0]) 
    & (round2ss["Top"]==datastring[1]) & (round2ss["C1"]==datastring[2])
    & (round2ss["C2"]==datastring[3]) & (round2ss["C3"]==datastring[4]) 
    & (round2ss["C4"]==datastring[5]) & (round2ss["C5"]==datastring[6])]
    Round2SSVal=Round2SSVal.reset_index(drop=True)
    Round2SSE = Round2SSVal["PctEuched"]
    Round2SSM = Round2SSVal["PctMajority"]
    Round2SS5 = Round2SSVal["PctAllFive"]
    Round2SSPts = Round2SSVal["ExpectedPoints"]
    Round2SSNum = Round2SSVal["TotOverall"]
    
    Round2SSLoneVal=round2sslone.loc[(round1lone["Pos"]==datastring[0]) & (round2sslone["Top"]==datastring[1])
                 & (round2sslone["C1"]==datastring[2])
                 & (round2sslone["C2"]==datastring[3]) & (round2sslone["C3"]==datastring[4]) 
                 & (round2sslone["C4"]==datastring[5]) & (round2sslone["C5"]==datastring[6])]
    Round2SSLoneVal=Round2SSLoneVal.reset_index(drop=True)
    Round2SSLoneE = Round2SSLoneVal["PctEuched"]
    Round2SSLoneM = Round2SSLoneVal["PctMajority"]
    Round2SSLone5 = Round2SSLoneVal["PctAllFive"]
    Round2SSLonePts = Round2SSLoneVal["ExpectedPoints"]
    Round2SSLoneNum = Round2SSLoneVal["TotOverall"]

    #Round 2 Offsuit1 Lookups-------------------------------------------------------------------------------
    Round2OS1Val=round2os1.loc[(round2os1["Pos"]==datastring[0]) 
    & (round2os1["Top"]==datastring[1]) & (round2os1["C1"]==datastring[2])
    & (round2os1["C2"]==datastring[3]) & (round2os1["C3"]==datastring[4]) 
    & (round2os1["C4"]==datastring[5]) & (round2os1["C5"]==datastring[6])]
    Round2OS1Val=Round2OS1Val.reset_index(drop=True)
    Round2OS1E = Round2OS1Val["PctEuched"]
    Round2OS1M = Round2OS1Val["PctMajority"]
    Round2OS15 = Round2OS1Val["PctAllFive"]
    Round2OS1Pts = Round2OS1Val["ExpectedPoints"]
    Round2OS1Num = Round2OS1Val["TotOverall"]
    
    Round2OS1LoneVal=round2os1lone.loc[(round2os1lone["Pos"]==datastring[0]) & (round2os1lone["Top"]==datastring[1])
                 & (round2os1lone["C1"]==datastring[2])
                 & (round2os1lone["C2"]==datastring[3]) & (round2os1lone["C3"]==datastring[4]) 
                 & (round2os1lone["C4"]==datastring[5]) & (round2os1lone["C5"]==datastring[6])]
    Round2OS1LoneVal=Round2OS1LoneVal.reset_index(drop=True)
    Round2OS1LoneE = Round2OS1LoneVal["PctEuched"]
    Round2OS1LoneM = Round2OS1LoneVal["PctMajority"]
    Round2OS1Lone5 = Round2OS1LoneVal["PctAllFive"]
    Round2OS1LonePts = Round2OS1LoneVal["ExpectedPoints"]
    Round2OS1LoneNum = Round2OS1LoneVal["TotOverall"]

    #Round 2 Offsuit2 Lookups-------------------------------------------------------------------------------
    Round2OS2Val=round2os2.loc[(round2os2["Pos"]==datastring[0]) 
    & (round2os2["Top"]==datastring[1]) & (round2os2["C1"]==datastring[2])
    & (round2os2["C2"]==datastring[3]) & (round2os2["C3"]==datastring[4]) 
    & (round2os2["C4"]==datastring[5]) & (round2os2["C5"]==datastring[6])]
    Round2OS2Val=Round2OS2Val.reset_index(drop=True)
    Round2OS2E = Round2OS2Val["PctEuched"]
    Round2OS2M = Round2OS2Val["PctMajority"]
    Round2OS25 = Round2OS2Val["PctAllFive"]
    Round2OS2Pts = Round2OS2Val["ExpectedPoints"]
    Round2OS2Num = Round2OS2Val["TotOverall"]
    
    Round2OS2LoneVal=round2os2lone.loc[(round1lone["Pos"]==datastring[0]) & (round2os2lone["Top"]==datastring[1])
                 & (round2os2lone["C1"]==datastring[2])
                 & (round2os2lone["C2"]==datastring[3]) & (round2os2lone["C3"]==datastring[4]) 
                 & (round2os2lone["C4"]==datastring[5]) & (round2os2lone["C5"]==datastring[6])]
    Round2OS2LoneVal=Round2OS2LoneVal.reset_index(drop=True)
    Round2OS2LoneE = Round2OS2LoneVal["PctEuched"]
    Round2OS2LoneM = Round2OS2LoneVal["PctMajority"]
    Round2OS2Lone5 = Round2OS2LoneVal["PctAllFive"]
    Round2OS2LonePts = Round2OS2LoneVal["ExpectedPoints"]
    Round2OS2LoneNum = Round2OS2LoneVal["TotOverall"]

    totHands = float(Round1Num) + float(Round1LoneNum) + float(Round2SSNum) + float(Round2SSLoneNum) + float(Round2OS1Num) + float(Round2OS1LoneNum)+ float(Round2OS2Num) + float(Round2OS2LoneNum)
    
    if ss == "Hearts" or ss == "Diamonds":
        stylecode1 = "Label2.TLabel"
        stylecode2 = "Label3.TLabel"
    elif ss == "Spades" or ss == "Clubs":
        stylecode1 = "Label3.TLabel"
        stylecode2 = "Label2.TLabel"
    
    ttk.Label(mainframe, text="Total Times This Exact Scenario Was Simulated: {}".format(int(totHands))).grid(column=1,row=1, columnspan=4,pady=5, rowspan=2)

    ttk.Label(mainframe, text="If Ordered Up:\nExpected Points:{:0.2f}".format(float(Round1Pts)),style=stylecode1).grid(column=1,row=5, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round1RegE)*100,float(Round1RegM)*100,float(Round1Reg5)*100)).grid(column=1,row=8, rowspan = 5)

    ttk.Label(mainframe, text="If Ordered Up ALONE:\nExpected Points:{:0.2f}".format(float(Round1LonePts)),style=stylecode1).grid(column=1,row=15, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round1LoneE)*100,float(Round1LoneM)*100,float(Round1Lone5)*100)).grid(column=1,row=18, rowspan = 5)
    
    ttk.Label(mainframe, text="If {} Called:\nExpected Points:{:0.2f}".format(ss,float(Round2SSPts)),style=stylecode1).grid(column=2,row=5, padx=10, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round2SSE)*100,float(Round2SSM)*100,float(Round2SS5)*100)).grid(column=2,row=8, padx=10, rowspan = 5)
    ttk.Label(mainframe, text="If {} Called ALONE:\nExpected Points:{:0.2f}".format(ss,float(Round2SSLonePts)),style=stylecode1).grid(column=2,row=15,padx = 10, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round2SSLoneE)*100,float(Round2SSLoneM)*100,float(Round2SSLone5)*100)).grid(column=2,row=18, padx=10, rowspan = 5)
    
    ttk.Label(mainframe, text="If {} Called:\nExpected Points:{:0.2f}".format(os1,float(Round2OS1Pts)),style=stylecode2).grid(column=3,row=5,padx=10, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round2OS1E)*100,float(Round2OS1M)*100,float(Round2OS15)*100)).grid(column=3,row=8,padx=10, rowspan = 5)
    ttk.Label(mainframe, text="If {} Called ALONE:\nExpected Points:{:0.2f}".format(os1,float(Round2OS1LonePts)),style=stylecode2).grid(column=3,row=15,padx=10, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round2OS1LoneE)*100,float(Round2OS1LoneM)*100,float(Round2OS1Lone5)*100)).grid(column=3,row=18, padx=10, rowspan = 5)
    
    ttk.Label(mainframe, text="If {} Called:\nExpected Points:{:0.2f}".format(os2,float(Round2OS2Pts)),style=stylecode2).grid(column=4,row=5, padx=10, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round2OS2E)*100,float(Round2OS2M)*100,float(Round2OS25)*100)).grid(column=4,row=8, padx=10, rowspan = 5)
    ttk.Label(mainframe, text="If {} Called ALONE:\nExpected Points:{:0.2f}".format(os2,float(Round2OS2LonePts)),style=stylecode2).grid(column=4,row=15, padx=10, rowspan = 3)
    ttk.Label(mainframe, text="Chance of:\n----Euched: {:0.2f}%\n----Majority: {:0.2f}%\n----All 5: {:0.2f}%".format(float(Round2OS2LoneE)*100,float(Round2OS2LoneM)*100,float(Round2OS2Lone5)*100)).grid(column=4,row=18,padx=10, rowspan = 5)

    return None

root = Tk()
root.title("Euchrevolution's Euchre Probability Lookup")
root.geometry('1150x450')

s = ttk.Style()
s.configure('Frame1.TFrame',background='green')
s.configure("Label1.TLabel", background="green")
s.configure("Label2.TLabel", background="red", width=25) #for hearts and diamonds
s.configure("Label3.TLabel", background="black", foreground="white", width=25) #for spades and clubs
mainframe = ttk.Frame(root, style="Frame1.TFrame")
mainframe.grid(column=0,row=0, padx=10,pady=10,sticky=(N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)
    
topcardrawval = StringVar()
topcard = StringVar()
card1raw = StringVar()
card2raw = StringVar()
card3raw = StringVar()
card4raw = StringVar()
card5raw = StringVar()
card1 = StringVar()
card2 = StringVar()
card3 = StringVar()
card4 = StringVar()
card5 = StringVar()
positionraw = StringVar()
position = StringVar()
    
topcardrawval_entry = ttk.Entry(mainframe, width = 5, textvariable =topcardrawval)
card1raw_entry = ttk.Entry(mainframe, width = 5, textvariable =card1raw)
card2raw_entry = ttk.Entry(mainframe, width = 5, textvariable =card2raw)
card3raw_entry = ttk.Entry(mainframe, width = 5, textvariable =card3raw)
card4raw_entry = ttk.Entry(mainframe, width = 5, textvariable =card4raw)
card5raw_entry = ttk.Entry(mainframe, width = 5, textvariable =card5raw)
positionraw_entry = ttk.Entry(mainframe, width= 5, textvariable = positionraw)
ttk.Label(mainframe, text="Top Card:").grid(row=7)
topcardrawval_entry.grid(column=0, row=8)
ttk.Label(mainframe, text="Cards in Hand:").grid(row=9)
card1raw_entry.grid(column=0, row=10)
card2raw_entry.grid(column=0, row=11)
card3raw_entry.grid(column=0, row=12)
card4raw_entry.grid(column=0, row=13)
card5raw_entry.grid(column=0, row=14)
ttk.Label(mainframe, text="Position (1 = Lead, 4 = Dealer):").grid(row=15)
positionraw_entry.grid(column=0, row=16)

#Getting Variables------------------------------------------------------------------
ttk.Label(mainframe, text="Directions for inputting cards:", style="Label1.TLabel").grid(row=0, sticky=(W))
ttk.Label(mainframe, text="Type the first letter of the card value, followed by the first letter of the suit", style="Label1.TLabel").grid(row=1, sticky=(W),padx=5)
ttk.Label(mainframe, text="For example: Ace of Hearts is \'AH\' (without the quotations, in capital letters)", style="Label1.TLabel").grid(row=2, sticky=(W))
ttk.Label(mainframe, text="For 9s and 10s, use N and T, respectively.", style="Label1.TLabel").grid(row=3, sticky=(W))
ttk.Label(mainframe, text="The order you input cards does not matter.", style="Label1.TLabel").grid(row=4, sticky=(W))

ttk.Label(mainframe, text="========================================RESULTS========================================", style="Label1.TLabel").grid(column=1,row=0,columnspan=4, pady=10, rowspan=2)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=0, row=20, pady=10)

for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=1)
topcardrawval_entry.focus()
card1raw_entry.focus()
card2raw_entry.focus()
card3raw_entry.focus()
card4raw_entry.focus()
card5raw_entry.focus()
positionraw_entry.focus()

root.bind('<Return>',calculate)


def main():
    root.mainloop()
    return None

if __name__ == "__main__":
    main()
    

    
