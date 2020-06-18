import random

STICKTHEDEALER = True
SHOWHAPPENINGS = True
PLAYER1 = "P1"
PLAYER2 = "P2"
PLAYER3 = "P3"
PLAYER4 = "P4"

PlayerHands = [[],[],[],[]]
Points = [0,0]

card_dict={0:"JT", 1:"JSS", 2:"AT", 3:"KT", 4:"QT", 5:"TT", 6:"NT", 7:"ASS",
         8:"KSS", 9:"QSS", 10:"TSS", 11:"NSS", 12:"AOS1", 13:"KOS1", 14:"QOS1",
         15:"JOS1", 16:"TOS1", 17:"NOS1", 18:"AOS2", 19:"KOS2", 20:"QOS2",
         21:"JOS2", 22:"TOS2", 23:"NOS2"}

#Declaring constant lists for easier use later on
OFFSUITA = [7,12,18]
OFFSUITK = [8,13,19]
OFFSUITQ = [9,14,20]
OFFSUITJ = [15,21]
OFFSUIT10 = [10,16,22]
OFFSUIT9 = [11,17,23]
OFFSUITS = [OFFSUIT9,OFFSUIT10,OFFSUITJ,OFFSUITQ,OFFSUITK,OFFSUITA]

def CountSuits(hand):
    """Counts the number of suits in a players hand"""
    numtrump = 0
    numss = 0
    numos1 = 0
    numos2 = 0

    for card in hand:
        if card < 7:
            numtrump += 1
        elif card < 12:
            numss += 1
        elif card < 18:
            numos1 += 1
        else:
            numos2 += 1
    
    numsuits = 0
    if numtrump != 0:
        numsuits += 1
    if numss != 0:
        numsuits += 1
    if numos1 != 0:
        numsuits += 1
    if numos2 != 0:
        numsuits += 1
    return [numtrump,numss,numos1,numos2,numsuits]

def Deal():
    """Deals Random Cards to Players' Hands"""
    cardsout = []
    cardoptions = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    topcardoptions = [0,2,3,4,5,6]
    topcard = topcardoptions[random.randint(0,5)]
    cardoptions.pop(cardoptions.index(topcard))
    cardsout.append(topcard)

    if SHOWHAPPENINGS == True:
        disp = card_dict[topcard]
        print("Topcard is: {}".format(disp)) 

    for i in range(4):
        numcards = 0
        while numcards < 5:
            possiblerange = len(cardoptions) - 1
            cardindex = random.randint(0,possiblerange)
            card = cardoptions[cardindex]
            cardsout.append(card)
            cardoptions.pop(cardoptions.index(card))
            PlayerHands[i].append(card)
            numcards += 1
        PlayerHands[i] = sorted(PlayerHands[i]) #putting into ascending order
        if i == 0 or i == 2:
            PlayerHands[i].append("RedTeam")
        else: 
            PlayerHands[i].append("BlackTeam")
    
    PlayerHands[0].append(PLAYER1)
    PlayerHands[1].append(PLAYER2)
    PlayerHands[2].append(PLAYER3)
    PlayerHands[3].append(PLAYER4)
    #PlayerHand format = [card1,card2,card3,card4,card5,Team,Name]

    return topcard

def OrderUpLogic(topcard,hand): #FIXME
    """Tells players whether to order up the top card or not"""

    order = 1 #FIXME

    return order

def CallSuitLogic(hand): #FIXME
    """Tells players what to order up trump as"""

    call = 0
    suit = 1

    return [call, suit]

def DealerLogic(hand):
    """Tells the dealer what card to discard, returns card value"""
    inithand = [0,0,0,0,0]
    temphand = [0,0,0,0,0]
    for j in range(5):
        inithand[j] = hand[j] #just numericalvalues of hand
        temphand[j] = hand[j]
    possiblecards = []
    basesuits = CountSuits(inithand)

    for i in range(5):
        for j in range(5):
            temphand[j] = inithand[j] #resetting for correct value
        temphand[i] = 0 #generic trump value for hand
        temphand = sorted(temphand) #putting in ascending order again
        temp = CountSuits(temphand)
        if temp[4] < basesuits[4]: #if by replacing that card, number of suits decreases 
            possiblecards.append(i) #save index of card  

    if len(possiblecards) == 0: #if can't decrease number of suits, tries to make as close to less suited
        if basesuits[4] == 1: #can't make less suited as all one suit already
            return max(inithand) #smallest card possible discarded
        elif basesuits[4] == 2: #two suited already (2 of 1 suit, 3 of other), can't make less suited
            discardsuit = basesuits.index(2) #finds suit that has 2
        else: #three suited, can't make less (1 trump, 2 of one, 2 of other)
            for i in range(len(OFFSUITS)):
                for j in range(len(OFFSUITS[i])):
                    if OFFSUITS[i][j] in inithand:
                        return OFFSUITS[i][j] #returning minimum offsuit card
        if discardsuit == 1: #discard ss
            return inithand[1] 
        elif discardsuit == 2: #discard os1
            if basesuits[1] != 0: #other option is ss
                return inithand[4]
            else: #other option is os2
                return inithand[1]
        else: #discard os2
            return inithand[4]
    elif len(possiblecards) == 1: #if only one card makes less suited
        return inithand[possiblecards[0]]
    else: #multiple choices on proper discard, discard lowest card
        for i in range(len(OFFSUITS)):
            for j in range(len(OFFSUITS[i])):
                if OFFSUITS[i][j] in inithand:
                    return OFFSUITS[i][j] #returning minimum offsuit card

def Calling(topcard):
    """Gives Players Option to Order Up
    or call suit if it comes to it"""
    calls = [0,0,0,0,0,0,0,0]
    desiredsuits = [0,0,0,0]

    for x in range(4):
       calls[x] = OrderUpLogic(topcard, PlayerHands[x])

    i = 0
    call = 0

    while i < 4:
        if calls[i] != 0: #If Called
            caller_id = PlayerHands[i][5]
            call = calls[i]
            discard = DealerLogic(PlayerHands[3]) #Dealer picks up card
            discard_index = PlayerHands[3].index(discard)
            PlayerHands[3][discard_index] = topcard
            trump = 0
            if SHOWHAPPENINGS == True:
                if call == 1:
                    disp1 = ""
                else: #Alone
                    disp1 = "Alone"
                print("{} orders up Dealer{}. Trump stays.".format(PlayerHands[i][6],disp1))
            i = 5
        else:
            i += 1
    
    if i == 4: #Not Ordered Up

        for k in range(4): #Filling with desired outcomes
            data = CallSuitLogic(PlayerHands[k])
            calls[k+4] = data[0]
            desiredsuits[k] = data[1]

        if calls[7] == 0 and STICKTHEDEALER == True: #Stick the dealer rule
            calls[7] = 1
        
        j = 4
        while j < 8:
            if calls[j] != 0: #If Called
                caller_id = PlayerHands[j-4][5]
                call = calls[j]
                trump = desiredsuits[j-4] 
                if SHOWHAPPENINGS == True:
                    if trump == 1:
                        disp = "Shortsuit"
                    elif trump == 2:
                        disp = "Offsuit1"
                    elif trump == 3:
                        disp = "Offsuit2"
                    else:
                        raise Exception("Error Code 09")
                    if call == 1:
                        disp2 = "Suit"
                    else: 
                        disp2 = "Alone"

                    print("{} Calls {}. {} is trump.".format(PlayerHands[i][6],disp2,disp))
                j = 9
            else:
                j += 1
        
        if j == 8: #Misdeal
            raise Exception("Misdeal and I haven't coded anything for this yet")
            #FIXME Maybe?

    call_data = [caller_id,call,trump]

    return call_data

def loneprocedure(): #FIXME
    #FIXME
    pass
    return None

def SetTrump(call_data):
    """Rotates numbers to corresponding simplified values"""
    trump = call_data[2]

    if trump == 0: #Ordered Up
        pass
    elif trump == 1: #SS
        for i in range(4):
            for j in range(5):
                if PlayerHands[i][j] < 12: #Only suits that flip
                    if PlayerHands[i][j] == 0:
                        PlayerHands[i][j] = 1
                    elif PlayerHands[i][j] == 1:
                        PlayerHands[i][j] = 0
                    elif PlayerHands[i][j] == 2:
                        PlayerHands[i][j] = 7
                    elif PlayerHands[i][j] == 3:
                        PlayerHands[i][j] = 8
                    elif PlayerHands[i][j] == 4:
                        PlayerHands[i][j] = 9
                    elif PlayerHands[i][j] == 5:
                        PlayerHands[i][j] = 10
                    elif PlayerHands[i][j] == 6:
                        PlayerHands[i][j] = 11
                    elif PlayerHands[i][j] == 7:
                        PlayerHands[i][j] = 2
                    elif PlayerHands[i][j] == 8:
                        PlayerHands[i][j] = 3
                    elif PlayerHands[i][j] == 9:
                        PlayerHands[i][j] = 4
                    elif PlayerHands[i][j] == 10:
                        PlayerHands[i][j] = 5
                    elif PlayerHands[i][j] == 11:
                        PlayerHands[i][j] = 6
                    else:
                        raise Exception("Unrecognized Card Value, Error Code 01")
    elif trump == 2: #OS1
        for i in range(4):
            for j in range(5):
                if PlayerHands[i][j] == 0:
                    PlayerHands[i][j] = 15
                elif PlayerHands[i][j] == 1:
                    PlayerHands[i][j] = 21
                elif PlayerHands[i][j] == 2:
                    PlayerHands[i][j] = 12
                elif PlayerHands[i][j] == 3:
                    PlayerHands[i][j] = 13
                elif PlayerHands[i][j] == 4:
                    PlayerHands[i][j] = 14
                elif PlayerHands[i][j] == 5:
                    PlayerHands[i][j] = 16
                elif PlayerHands[i][j] == 6:
                    PlayerHands[i][j] = 17
                elif PlayerHands[i][j] == 7:
                    PlayerHands[i][j] = 18
                elif PlayerHands[i][j] == 8:
                    PlayerHands[i][j] = 19
                elif PlayerHands[i][j] == 9:
                    PlayerHands[i][j] = 20
                elif PlayerHands[i][j] == 10:
                    PlayerHands[i][j] = 22
                elif PlayerHands[i][j] == 11:
                    PlayerHands[i][j] = 23
                elif PlayerHands[i][j] == 12:
                    PlayerHands[i][j] = 2
                elif PlayerHands[i][j] == 13:
                    PlayerHands[i][j] = 3
                elif PlayerHands[i][j] == 14:
                    PlayerHands[i][j] = 4
                elif PlayerHands[i][j] == 15:
                    PlayerHands[i][j] = 0
                elif PlayerHands[i][j] == 16:
                    PlayerHands[i][j] = 5
                elif PlayerHands[i][j] == 17:
                    PlayerHands[i][j] = 6
                elif PlayerHands[i][j] == 18:
                    PlayerHands[i][j] = 7
                elif PlayerHands[i][j] == 19:
                    PlayerHands[i][j] = 8
                elif PlayerHands[i][j] == 20:
                    PlayerHands[i][j] = 9
                elif PlayerHands[i][j] == 21:
                    PlayerHands[i][j] = 1
                elif PlayerHands[i][j] == 22:
                    PlayerHands[i][j] = 10
                elif PlayerHands[i][j] == 23:
                    PlayerHands[i][j] = 11
                else:
                    raise Exception("Unrecognized Card Value, Error Code 02")
    else: #trump == OS2
        for i in range(4):
            for j in range(5):
                if PlayerHands[i][j] == 0:
                    PlayerHands[i][j] = 15
                elif PlayerHands[i][j] == 1:
                    PlayerHands[i][j] = 21
                elif PlayerHands[i][j] == 2:
                    PlayerHands[i][j] = 12
                elif PlayerHands[i][j] == 3:
                    PlayerHands[i][j] = 13
                elif PlayerHands[i][j] == 4:
                    PlayerHands[i][j] = 14
                elif PlayerHands[i][j] == 5:
                    PlayerHands[i][j] = 16
                elif PlayerHands[i][j] == 6:
                    PlayerHands[i][j] = 17
                elif PlayerHands[i][j] == 7:
                    PlayerHands[i][j] = 18
                elif PlayerHands[i][j] == 8:
                    PlayerHands[i][j] = 19
                elif PlayerHands[i][j] == 9:
                    PlayerHands[i][j] = 20
                elif PlayerHands[i][j] == 10:
                    PlayerHands[i][j] = 22
                elif PlayerHands[i][j] == 11:
                    PlayerHands[i][j] = 23
                elif PlayerHands[i][j] == 12:
                    PlayerHands[i][j] = 7
                elif PlayerHands[i][j] == 13:
                    PlayerHands[i][j] = 8
                elif PlayerHands[i][j] == 14:
                    PlayerHands[i][j] = 9
                elif PlayerHands[i][j] == 15:
                    PlayerHands[i][j] = 1
                elif PlayerHands[i][j] == 16:
                    PlayerHands[i][j] = 10
                elif PlayerHands[i][j] == 17:
                    PlayerHands[i][j] = 11
                elif PlayerHands[i][j] == 18:
                    PlayerHands[i][j] = 2
                elif PlayerHands[i][j] == 19:
                    PlayerHands[i][j] = 3
                elif PlayerHands[i][j] == 20:
                    PlayerHands[i][j] = 4
                elif PlayerHands[i][j] == 21:
                    PlayerHands[i][j] = 0
                elif PlayerHands[i][j] == 22:
                    PlayerHands[i][j] = 5
                elif PlayerHands[i][j] == 23:
                    PlayerHands[i][j] = 6
                else:
                    raise Exception("Unrecognized Card Value, Error Code 03")                

    return None

def EndHand(redtricks, blacktricks):
    """Can end hand early if it doesn't need to be played out"""
    if redtricks >= 3 and blacktricks == 1:
        return True
    elif blacktricks >= 3 and redtricks == 1:
        return True
    elif (redtricks + blacktricks) == 5:
        return True
    else:
        return False

def DetermineWinner(trickcards):
    """Takes in Cards played in a trick
    and returns the winner's index"""

    if trickcards[0] <= 6: #Trump Led
        winner = trickcards.index(min(trickcards))
    elif trickcards[0] > 6 and trickcards[0] < 12: #Shortsuit led
        winner = trickcards.index(min(trickcards))
    elif trickcards[0] > 11 and trickcards[0] < 18: #Offsuit1 led
        winner = trickcards[0]
        for i in range(3):
            if trickcards[i+1] < winner and (trickcards[i+1] < 7 or trickcards[i+1] > 11):
                winner = trickcards[i+1]
        winner = trickcards.index(winner)
    else: #Offsuit 2 led
        winner = trickcards[0]
        for i in range(3):
            if trickcards[i+1] < winner and (trickcards[i+1] < 7 or trickcards[i+1] > 17):
                winner = trickcards[i+1]
        winner = trickcards.index(winner)

    return winner

def BestPlay(cardsout, trickcards,hand): #FIXME
    """Main decision making function for players to choose what card to play"""

    trump = []
    ss = []
    os1 = []
    os2 = []

    for i in range(len(hand) - 2):
        if hand[i] < 7:
            trump.append(hand[i])
        elif hand[i] < 12:
            ss.append(hand[i])
        elif hand[i] < 18:
            os1.append(hand[i]) 
        else: 
            os2.append(hand[i])

    if len(trickcards) == 0: #Lead
        return 0 #FIXME-----------------------------------------------------------
    else: #Not lead
        if trickcards[0] < 7: #Trump led
            if len(trump) == 1:
                return hand.index(trump[0])
            #Led trump decision play FIXME---------------------------------
        elif trickcards[0] < 12: #SS led
            if len(ss) == 1:
                return hand.index(ss[0])
            #Led ss decision FIXME-------------------------------------------------
        elif trickcards[0] < 18: #OS1 led
            if len(os1) == 1:
                return hand.index(os1[0])
            #Led os1 decision FIXME--------------------------------------------
        else: #OS2 led
            if len(os2) == 1:
                return hand.index(os2[0]) 
            #led os2 decision FIXME--------------------------------------------
 
    return 0

def PointsEarned(redtricks, blacktricks, call_data):
    """Determines points earned depending on who called,
    what was called, and number of tricks earned"""

    if call_data[1] == 1: #Normal Call
        if call_data[0] == "RedTeam":
            if redtricks == 5:
                winner = 0
                points = 2
            elif redtricks > 2:
                winner = 0
                points = 1
            else: #Euched
                winner = 1
                points = 2
        elif call_data[0] == "BlackTeam":
            if blacktricks == 5:
                winner = 1
                points = 2
            elif blacktricks > 2:
                winner = 1
                points = 1
            else: #Euched
                winner = 0
                points = 2  
    else: #Loner
        if call_data[0] == "RedTeam":
            if redtricks == 5:
                winner = 0
                points = 4
            elif redtricks > 2:
                winner = 0
                points = 1
            else: #Euched
                winner = 1
                points = 2
        elif call_data[0] == "BlackTeam":
            if blacktricks == 5:
                winner = 1
                points = 4
            elif blacktricks > 2:
                winner = 1
                points = 1
            else: #Euched
                winner = 0
                points = 2
        else:
            raise Exception("Error Code 07")

    return [winner, points]

def RotateLead(winner,tricksplayed):
    """Function to rotate lead depending on winner"""
    temps = [[],[],[],[]]

    if winner == 0:
        return None
    else: #Need to rotate
        for i in range(4):
            for j in range(7-tricksplayed):
                temps[i].append(PlayerHands[i][j])
        
        if winner == 1:
            for j in range(7 - tricksplayed):
                PlayerHands[0][j] = temps[1][j]
                PlayerHands[1][j] = temps[2][j]
                PlayerHands[2][j] = temps[3][j]
                PlayerHands[3][j] = temps[0][j]
        
        elif winner == 2:
            for j in range(7 - tricksplayed):
                PlayerHands[0][j] = temps[2][j]
                PlayerHands[1][j] = temps[3][j]
                PlayerHands[2][j] = temps[0][j]
                PlayerHands[3][j] = temps[1][j]

        else:
            for j in range(7 - tricksplayed):
                PlayerHands[0][j] = temps[3][j]
                PlayerHands[1][j] = temps[0][j]
                PlayerHands[2][j] = temps[1][j]
                PlayerHands[3][j] = temps[2][j]

    return None

def SetOrder(lastdealer):
    """Sets the player order"""
    if Points[0] == 0 and Points[1] == 0: #Start of game
        startingdealer = random.randint(0,3)
        RotateLead(startingdealer,0)
        if SHOWHAPPENINGS == True:
            print("{} is Dealer".format(PlayerHands[3][6]))
    
    else: #Normal Hand
        if lastdealer == PLAYER1: #Player1 becomes lead
            pass #Deal should be correct
        elif lastdealer == PLAYER2:
            RotateLead(1,0)
        elif lastdealer == PLAYER3:
            RotateLead(2,0)
        elif lastdealer == PLAYER4:
            RotateLead(3,0)
        else: #Should not reach here
            raise Exception("Error Code 10")
        
        if SHOWHAPPENINGS == True:
            print("{} is Dealer".format(PlayerHands[3][6]))

    return None

def GamePlay():
    """Playing the Game"""
    
    cardsout = []
    redtricks = 0
    blacktricks = 0
    trickcards = []
    tricksplayed = 0
    lastdealer = PlayerHands[3][6]

    while not EndHand(redtricks,blacktricks): #Computing to see if trick can end early
        while tricksplayed < 5: #5 tricks max
            for j in range(4):
                play = BestPlay(cardsout,trickcards,PlayerHands[j])
                card = PlayerHands[j][play]
                cardsout.append(card)
                trickcards.append(card)
                PlayerHands[j].pop(play)
 
            winner = DetermineWinner(trickcards)
            
            if SHOWHAPPENINGS == True:
                for k in range(4):
                    trickcards[k] = card_dict[trickcards[k]]
                    print("{} plays {}.".format(PlayerHands[k][-1], trickcards[k]))
                print("{} takes trick\n".format(PlayerHands[winner][-1]))

            if PlayerHands[winner][-2] == "RedTeam": 
                redtricks = redtricks + 1
            elif PlayerHands[winner][-2] == "BlackTeam":
                blacktricks = blacktricks + 1
            else: 
                raise Exception("Error Code 06")

            tricksplayed = tricksplayed + 1   

            RotateLead(winner, tricksplayed)
            
            x = 0
            while x < 4:
                trickcards.pop(0) #Resetting trick
                x = x+1

    return [redtricks,blacktricks,lastdealer]

def Addpoints(points):
    """Adds points to appropriate score"""
    #points = [winner, points]
    if points[0] == 0:
        Points[0] = Points[0] + points[1]
    elif points[0] == 1:
        Points[1] = Points[1] + points[1]
    else:
        raise Exception("Error Code 04")

    return None

def main():
    """Main Function"""
    lastdealer = 0

    while Points[0] < 10 and Points[1] < 10:
        topcard = Deal()
        SetOrder(lastdealer)
        call_data = Calling(topcard)
        SetTrump(call_data)
        winner_data = GamePlay()
        lastdealer = winner_data[2]
        points = PointsEarned(winner_data[0], winner_data[1], call_data)
        Addpoints(points)
        for i in range(4):
            PlayerHands[i].pop(1)
            PlayerHands[i].pop(0)
        if SHOWHAPPENINGS == True:
            print("Current Score: Red: {}, Black: {}".format(Points[0],Points[1]))

    if SHOWHAPPENINGS == True:
        print("\n\nFinal Score: Red: {}, Black: {}".format(Points[0],Points[1]))

    return None

main()