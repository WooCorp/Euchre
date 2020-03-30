# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:22:37 2020

@author: Ben Gochanour
"""
import os
import pandas as pd
os.chdir("C:\\Users\\Ben Gochanour\\Documents\\GitHub\\EuchreBot\\Order Up Final Results\\Round 1")

# These deal with OrderUpLogic function
round1reglookup=pd.read_csv("Round1_OrderUp_round1reglookups.csv")
round1lonelookup=pd.read_csv("Round1_Loner_FinalResults.csv")

round1reglookup.head()

hand=[3,15,13,7,20]
pos=0 #Figure out where we derive this from
topcard=5 
thresh=0
hand=hand[0:5]
hand.sort()

def OrderUpLogic(topcard,pos,hand,thresh):
    hand=hand[0:5]
    hand.sort()
    Round1RegVal=round1reglookup.loc[(round1reglookup["Pos"]==pos) 
    & (round1reglookup["Top"]==topcard) & (round1reglookup["C1"]==hand[0])
    & (round1reglookup["C2"]==hand[1]) & (round1reglookup["C3"]==hand[2]) 
    & (round1reglookup["C4"]==hand[3]) & (round1reglookup["C5"]==hand[4])]['ExpectedPoints']
    Round1RegVal=Round1RegVal.reset_index(drop=True)
    Round1RegVal=float(Round1RegVal[0])
    
    Round1LoneVal=round1lonelookup.loc[(round1lonelookup["Pos"]==pos) & (round1lonelookup["Top"]==topcard)
                 & (round1lonelookup["C1"]==hand[0])
                 & (round1lonelookup["C2"]==hand[1]) & (round1lonelookup["C3"]==hand[2]) 
                 & (round1lonelookup["C4"]==hand[3]) & (round1lonelookup["C5"]==hand[4])]['ExpectedPoints']
    
    Round1LoneVal=Round1LoneVal.reset_index(drop=True)
    Round1LoneVal=float(Round1LoneVal[0])
    
    round1dict={Round1RegVal:'Reg',Round1LoneVal:'Lone'}
    
    if round1dict.get(max(round1dict))=="Reg":
        if Round1RegVal>thresh:
            call=1 #Reg
        else:
            call=0
    elif round1dict.get(max(round1dict))=="Lone":
        if Round1RegVal>thresh:
            call=2 #Lone
        else:
            call=0
    return call

OrderUpLogic(topcard=topcard,pos=pos,hand=hand,thresh=thresh)
    



# These deal with CallSuit Logic
os.chdir("C:\\Users\\Ben Gochanour\\Documents\\GitHub\\EuchreBot\\Order Up Final Results\\Round 2")
