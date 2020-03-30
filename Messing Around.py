# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:44:32 2020

@author: Ben Gochanour
"""

import numpy as np

# For Round 1

def Diff(list1, list2):
    return [i-j for i,j in zip(list1,list2)]

#def find(list, num=one):
 #   for i, sublist in enumerate(list):
  #      if one in sublist:
   #         print([i, sublist.index(one)])
# Works except for second or third of suit
   
def my_mapping(number):
    if number==8:
        i,j=[1,4] # Ace of SS is 8 which is in list[1][4]
        return [i,j]
    # Do this for everything
# Instead of find function, assume we know numbers of cards in our hand, in this case
# 6,8,9,etc.


TotUnknown=18
UnknownCards=[[1,1,1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]] # Order up R Bower
MyHand=[[1,0,0,0,0,0,0],[0,0,0,1,1],[0,0,0,1,0,0],[1,0,0,0,0,0]] # 9 of trump, etc.
UnknownCards=[Diff(l1,l2) for l1,l2 in zip(UnknownCards,MyHand)] # Update Unknown Cards
np.count_nonzero(UnknownCards[0]) #This is our equivalent len function for num remaining.

# Compute probs of winning:
# How many cards are to the left of (better than) ace of SS within the sublist?
# Our mapping fun has yielded a result, call it result=[i,j]
#result=my_mapping(8)
result=my_mapping(8)
i=result[0]
j=result[1]

# Then number of superior cards is
my_list=[UnknownCards[i][ind] for ind in range(0,j)]
n_better=sum(my_list) # this says 3 unknown cards better than us

# Prob must follow lower for first opponent
P_A=(1-((TotUnknown-n_better)/(TotUnknown)*(TotUnknown-n_better-1)/(TotUnknown-1)
*(TotUnknown-n_better-2)/(TotUnknown-2)*(TotUnknown-n_better-3)/(TotUnknown-3)*
(TotUnknown-n_better-4)/(TotUnknown-4)))

#P_B Continue on like this


# P_Winner=P_A*P_B

# Can also do this for trump too but don't want to burn



        
        
    return result

sum(range(4,8))
TotUnknown+=-3 # Subtract 3 from TotUnkown


