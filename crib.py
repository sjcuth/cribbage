import random

"""crib module. Contains classes Card, Hand, FullHand, Pegging, Deck"""

class Card:
    """Card class: has properties strRank, strSuit, suitNum, rankNum, value, rankString, suitString - has method for print override"""
    def __init__(self,strDef):
        """__init__(strDef): create a Card object with many properties based on an input strDef such as 'Ks' for King of Spades or 10h for 10 of Hearts"""
        self.strRank = strDef[0:-1]
        self.strSuit = strDef[-1]        

        #1-clubs 2-diamonds 3-hearts 4-spades 
        if self.strSuit=='c':
            self.suitNum=1
        elif self.strSuit=='d':
            self.suitNum=2
        elif self.strSuit=='h':
            self.suitNum=3
        elif self.strSuit=='s':
            self.suitNum=4

        #1-ace ... 13-king
        if self.strRank=='K':
            self.rankNum=13
        elif self.strRank=='Q':
            self.rankNum=12
        elif self.strRank=='J':
            self.rankNum=11
        elif self.strRank=='A':
            self.rankNum=1
        else:
            self.rankNum=int(self.strRank)

        #value of a card in cribbing and creating 15s
        if self.rankNum<=10:
            self.value = self.rankNum
        elif self.rankNum>=11:
            self.value = 10

        #string word for rank
        if self.rankNum == 1:
            rs='Ace'
        elif self.rankNum == 2:
            rs='Two'
        elif self.rankNum == 3:
            rs='Three'
        elif self.rankNum == 4:
            rs='Four'
        elif self.rankNum == 5:
            rs='Five'
        elif self.rankNum == 6:
            rs='Six'
        elif self.rankNum == 7:
            rs='Seven'
        elif self.rankNum == 8:
            rs='Eight'
        elif self.rankNum == 9:
            rs='Nine'
        elif self.rankNum == 10:
            rs='Ten'
        elif self.rankNum == 11:
            rs='Jack'
        elif self.rankNum == 12:
            rs='Queen'
        elif self.rankNum == 13:
            rs='King'            
        self.rankString = rs

        #string word for suit
        if self.suitNum == 1:
            ss='Clubs'
        elif self.suitNum == 2:
            ss='Diamonds'
        elif self.suitNum == 3:
            ss='Hearts'
        elif self.suitNum == 4:
            ss='Spades' 
        self.suitString = ss
        
    def __str__(self):
        """__str__(): override the print method for a Card """
        return self.rankString + ' of ' + self.suitString + ' - ' + self.strRank + self.strSuit + " - Suit Num: " + str(self.suitNum) + " Rank Num: " + str(self.rankNum) + " Point Value: " + str(self.value)
    
class Hand:
    """Hand class: has properties cards - has methods fillHand(card1,card2,card3,card4), calcPoints(deckCard,is_crib)"""
    def __init__(self):
        """__init__(): the Hand object will hold 4 card objects in this list """
        self.cards = []

            
    def fillHand(self,card1,card2,card3,card4):
        """fillHand(card1,card2,card3,card4): 4 card objects are placed in the cards list """
        del self.cards[0:]
       
        c1 = Card(card1)
        c2 = Card(card2)
        c3 = Card(card3)
        c4 = Card(card4)
        
        self.cards.append(c1)
        self.cards.append(c2)
        self.cards.append(c3)
        self.cards.append(c4)
 
        return self


    def calcPoints(self,deckCard,is_crib):
        """calcPoints(deckCard,is_crib): using the Hand cards list, this method will use a deckCard Card object and an is_crib boolean to calculate the points in a 5-card hand """
        self.deckCard = Card(deckCard)
        self.allCards = []
        for card in self.cards:
            self.allCards.append(card)
        self.allCards.append(self.deckCard)

        pointValue = 0
##        print(self.cards[0])
##        print(self.cards[1])
##        print(self.cards[2])
##        print(self.cards[3])
##        print(deckCard)

        
        #check for nob
        for card in self.cards:
            if card.rankNum==11 and card.suitNum == self.deckCard.suitNum:
                pointValue += 1

        #calculate flush points - a crib can only score 5, a hand can score 4 or 5
        if is_crib:
            if self.allCards[0].suitNum == self.allCards[1].suitNum and self.allCards[1].suitNum == self.allCards[2].suitNum and self.allCards[2].suitNum == self.allCards[3].suitNum  and self.allCards[3].suitNum == self.allCards[4].suitNum:
                pointValue +=5
        else:
            if self.allCards[0].suitNum == self.allCards[1].suitNum and self.allCards[1].suitNum == self.allCards[2].suitNum and self.allCards[2].suitNum == self.allCards[3].suitNum:
                pointValue +=4
                if self.allCards[0].suitNum == self.allCards[4].suitNum:
                    pointValue +=1            
                
        #sort list based on rankNum property - deck card no longer matters
        self.allCards.sort( key = lambda x: x.rankNum )

        #check runs
        if self.allCards[0].rankNum == self.allCards[1].rankNum - 1 and self.allCards[1].rankNum == self.allCards[2].rankNum - 1 and self.allCards[2].rankNum == self.allCards[3].rankNum - 1 and self.allCards[3].rankNum == self.allCards[4].rankNum - 1:
            pointValue += 5
        else:
            fourRun = False
            x=0   
            for card in self.allCards:
                newList=[]  
                for c in self.allCards:
                    if c != card:
                        newList.append(c)
                #print( str(len( newList )) + ' in the newList' )
                if newList[0].rankNum == newList[1].rankNum - 1 and newList[1].rankNum == newList[2].rankNum - 1 and newList[2].rankNum == newList[3].rankNum - 1:
                    pointValue += 4
                    fourRun = True

            if fourRun == False:
                x=0
                for card1 in self.allCards[x:-2]:
                    y=x+1
                    for card2 in self.allCards[y:-1]:
                        z=y+1
                        for card3 in self.allCards[z:]:
                            if card1.rankNum == card2.rankNum - 1 and card2.rankNum == card3.rankNum - 1:
                                pointValue+=3
                        y+=1
                    x+=1
                
            

        #check pairs and 2-card 15s
        x = 0
        for card1 in self.allCards[x:-1]:
            y = x + 1   
            for card2 in self.allCards[y:]:
                #print( str(card1.rankNum) + '-' + str(card2.rankNum) )
                if card1.rankNum == card2.rankNum:
                    pointValue += 2
                if card1.value + card2.value == 15:
                    pointValue += 2

                y += 1
                
            x += 1

        #check 3-card 15s
        x = 0
        for card1 in self.allCards[x:-2]:
            y = x+1
            for card2 in self.allCards[y:-1]:
                z = y+1
                for card3 in self.allCards[z:]:
                    #print( str(card1.rankNum) + '-' + str(card2.rankNum) + '-' + str(card3.rankNum) )

                    #15s
                    if card1.value + card2.value + card3.value == 15:
                        pointValue += 2                    
        
                    z+=1
                y+=1
            x+=1

        #check 4-card 15s
        x=0
        for card in self.allCards:
            sumValue = 0
            for c in self.allCards:
                if self.allCards[x] != c:
                    sumValue+=c.value
            
            if sumValue == 15:
                pointValue += 2

            x+=1

        #check 5-card 15
        sumValue = 0
        for card in self.allCards:
            sumValue += card.value
        if sumValue == 15:
            pointValue += 2

        self.allCards.remove(self.deckCard)
                        
        #print( pointValue)
        return pointValue


class FullHand:
    """FullHand class: has properties fullHandCards - has methods simulate(my_crib) """
    def __init__(self,card1,card2,card3,card4,card5,card6):
        """__init__(card1,card2,card3,card4,card5,card6): create a FullHand object consisting of 6 cards that have been dealt """
        self.fullHandCards = []

        self.fullHandCards.append( Card(card1) )
        self.fullHandCards.append( Card(card2) )
        self.fullHandCards.append( Card(card3) )
        self.fullHandCards.append( Card(card4) )
        self.fullHandCards.append( Card(card5) )
        self.fullHandCards.append( Card(card6) )

        
    def simulate(self,my_crib):
        """simulate(my_crib): input the my_crib boolean to simulate the decision that must be made on which 2 cards to discard into the crib """
        crib_simulations = 2000
        pegging_simulations = 2000
        max_points = 0
        h1 = Hand()
        h2 = Hand()
                
        x=0
        for discard1 in self.fullHandCards[x:5]:
            y=x+1
            for discard2 in self.fullHandCards[y:]:

                handCards = self.fullHandCards[:]
                handCards.remove(discard1)
                handCards.remove(discard2)

                my_c1 = Card(handCards[0].strRank + handCards[0].strSuit)
                my_c2 = Card(handCards[1].strRank + handCards[1].strSuit)
                my_c3 = Card(handCards[2].strRank + handCards[2].strSuit)
                my_c4 = Card(handCards[3].strRank + handCards[3].strSuit)

                h1.fillHand( handCards[0].strRank + handCards[0].strSuit,handCards[1].strRank + handCards[1].strSuit,handCards[2].strRank + handCards[2].strSuit,handCards[3].strRank + handCards[3].strSuit)

                d1 = Deck()
                d2 = Deck()
                for c in self.fullHandCards:
                    for d in d1.cards:
                        if c.suitNum==d.suitNum and c.rankNum==d.rankNum:
                            d1.cards.remove(d)
                            break

                pcount=0
                psum=0
                cribcount=0
                cribsum=0
                pegcount = 0
                pegsum = 0
                
                simulation_number = 0
                peg_simulation_number = 0
                
                for c in d1.cards:
                    psum += h1.calcPoints( c.strRank + c.strSuit, False )
                    pcount += 1

                while simulation_number < crib_simulations:
                    d2.cards = d1.cards[:]
                    
                    random1 = random.randint(0, len(d2.cards)-1 )
                    c2 = d2.cards[random1]
                    del d2.cards[random1]

                    random2 = random.randint(0, len(d2.cards)-1 )
                    c3 = d2.cards[random2]
                    del d2.cards[random2]

                    random3 = random.randint(0, len(d2.cards)-1 )
                    c4 = d2.cards[random3]
                    del d2.cards[random3]
                    

                    h2.fillHand( c2.strRank + c2.strSuit,c3.strRank + c3.strSuit,discard1.strRank + discard1.strSuit,discard2.strRank + discard2.strSuit )
                    cribsum += h2.calcPoints(c4.strRank + c4.strSuit, True)
                    cribcount+=1

                    simulation_number += 1

                while peg_simulation_number < pegging_simulations:
                    d2.cards = d1.cards[:]

                    #print("d2 card count:", len(d2.cards))
                    
                    random1 = random.randint(0, len(d2.cards)-1 )
                    c2 = d2.cards[random1]
                    del d2.cards[random1]

                    random2 = random.randint(0, len(d2.cards)-1 )
                    c3 = d2.cards[random2]
                    del d2.cards[random2]

                    random3 = random.randint(0, len(d2.cards)-1 )
                    c4 = d2.cards[random3]
                    del d2.cards[random3]

                    random4 = random.randint(0, len(d2.cards)-1 )
                    c5 = d2.cards[random4]
                    del d2.cards[random4]

##                    print(c2)
##                    print(c3)
##                    print(c4)
##                    print(c5)

                    p1 = Pegging()
                    pegsum += p1.pegSimulate( [my_c1,my_c2,my_c3,my_c4] , [c2,c3,c4,c5] , my_crib)
                    pegcount += 1

                    peg_simulation_number += 1                    

                avg_hand_points = round(psum / pcount,2)

                if my_crib:
                    avg_crib_points = round(cribsum / cribcount,2)
                else:
                    avg_crib_points = round(cribsum / cribcount,2) * -1

                avg_peg_points = round(pegsum / pegcount,2)
        
                
                print( "throwing", discard1.strRank + discard1.strSuit, discard2.strRank + discard2.strSuit, "+ keeping", handCards[0].strRank + handCards[0].strSuit,handCards[1].strRank + handCards[1].strSuit,handCards[2].strRank + handCards[2].strSuit,handCards[3].strRank + handCards[3].strSuit, "=avg hand points:", avg_hand_points, "+ average crib points of:", avg_crib_points, "+ net pegging points:" , avg_peg_points, "+ total points of:", round(avg_hand_points + avg_crib_points + avg_peg_points,2) )

                total_points = avg_hand_points + avg_crib_points + avg_peg_points

                if total_points > max_points:
                    max_points = total_points
                    throwCard1 = discard1
                    throwCard2 = discard2
                
            x+=1

        return throwCard1, throwCard2



class Pegging:
    """Pegging class: has properties None - has methods pegDecision(listMyHand, listPreviousCardsPlayed), pegSimulate(listMyHand,listOppHand,my_crib) """
    def __init__(self):
        """there are no class properties to initialize """
        pass

##        self.listPreviousCardsPlayed = []
##        self.listMyHand = []
##        self.listOppHand = []
##        self.pegCount = 0

##    def pegDecision(self,listMyHand,listOppHand, listPreviousCardsPlayed):
    def pegDecision(self, listMyHand, listPreviousCardsPlayed):     #consider checking for 31 as the top priority - but be careful to count runs and pairs if a 31 is made
        """pegDecision(listMyHand, listPreviousCardsPlayed): based on a list of cards in my hand during pegging and a list of cards currently played during pegging, make a decision about which card to play and returns it along with how many points were pegged """
        pegCount = 0
        for c in listPreviousCardsPlayed:
            pegCount+=c.value

        #print('Peg count: ' + str(pegCount))

        pointsPegged = 0

        #create two infeasibleListHands and remove infeasible cards from both hands - prohibited by >31
        listMySurvivors = [ c for c in listMyHand if c.value + pegCount <= 31 ]     #comprehension to remove while looping
        #listOppSurvivors = [ c for c in listOppHand if c.value + pegCount <= 31 ]   #comprehension to remove while looping
        
##        print('My surviving cards')
##        for c in listMySurvivors:
##            print(c)
##
##        print('Opponent surviving cards')
##        for c in listOppSurvivors:
##            print(c)
             
        if len(listMySurvivors) == 0:
            chosenCard = None
        else:

            runDetected = False
            pairDetected = False
            fifteenDetected = False
            thirtyoneDetected = False
                
            #check for run
            if len(listPreviousCardsPlayed) >=2:
                for r in range( len(listPreviousCardsPlayed)+1, 2, -1 ):
                    #print(r, "is the run length being tested")
                    for c in listMySurvivors:
                        testRun = listPreviousCardsPlayed[-(r-1):]
                        testRun.append(c)
                        testRun.sort( key = lambda x: x.rankNum )

##                        print('testRun cards')
##                        for g in testRun:
##                            print(g)
                        
                        for t in range( r-1 ):
                            #print("t is now", t)
                            if testRun[t].rankNum + 1 == testRun[t+1].rankNum:
                                runDetected = True
                            else:
                                runDetected = False
                                break
                        if runDetected:
                            chosenCard = c
                            #print(chosenCard)
                            pointsPegged = r
                            if pegCount + chosenCard.value == 15 or pegCount + chosenCard.value == 31:
                                pointsPegged += 2
                            
                            #print("Points pegged:", pointsPegged)
                            break

                    if runDetected:
                        break

##                if runDetected:
##                    print("A run was found")
##                else:
##                    print("No run was found")

            #check for pair
            if not runDetected and len(listPreviousCardsPlayed) >=1:
                for c in listMySurvivors:
                    if c.rankNum == listPreviousCardsPlayed[-1].rankNum:
                        chosenCard = c
                        #print(chosenCard)
                        pointsPegged = 2
                        if len(listPreviousCardsPlayed) >= 2 and listPreviousCardsPlayed[-1].rankNum == listPreviousCardsPlayed[-2].rankNum:
                            pointsPegged = 6
                        if len(listPreviousCardsPlayed) >= 3 and listPreviousCardsPlayed[-1].rankNum == listPreviousCardsPlayed[-2].rankNum and listPreviousCardsPlayed[-2].rankNum == listPreviousCardsPlayed[-3].rankNum:
                            pointsPegged = 12
                        #print("Points pegged:", pointsPegged)
                        if pegCount + chosenCard.value == 15 or pegCount + chosenCard.value == 31:
                            pointsPegged += 2
                        pairDetected = True
                        break
                    
##                if pairDetected:
##                    print("A pair was found")
##                else:
##                    print("No pair was found")

            #check for 15
            if not runDetected and not pairDetected and len(listPreviousCardsPlayed) >=1:
                for c in listMySurvivors:
                    if c.value + pegCount == 15:
                        chosenCard = c
                        #print(chosenCard)
                        pointsPegged = 2
                        #print("Points pegged:", pointsPegged)
                        fifteenDetected = True
                        break
                    
##                if fifteenDetected:
##                    print("A 15 was found")
##                else:
##                    print("No 15 was found")

            #check for 31
            if not runDetected and not pairDetected and not fifteenDetected and len(listPreviousCardsPlayed) >= 3:
                for c in listMySurvivors:
                    if c.value + pegCount == 31:
                        chosenCard = c
                        #print(chosenCard)
                        pointsPegged = 2
                        #print("Points pegged:", pointsPegged)
                        thirtyoneDetected = True
                        break
                    
##                if thirtyoneDetected:
##                    print("A 31 was found")
##                else:
##                    print("No 31 was found")

            #otherwise strategize point ranges knowing that you can't score right now
            if not runDetected and not pairDetected and not fifteenDetected and not thirtyoneDetected:

                listMySurvivors.sort( key = lambda x: x.rankNum )
                listMySurvivors.reverse()

##                print('My reverse sorted surviving cards')
##                for c in listMySurvivors:
##                    print(c)

                chosenCard = listMySurvivors[0]                       

##                print('Previous Cards Played')
##                for c in listPreviousCardsPlayed:
##                    print(c)


                if pegCount<=4:    #keep out of 15 range

                    if pegCount == 0:

                        for c in listMySurvivors:
                            if c.value < 5:
                                chosenCard = c
                                break
                            elif c.value > 5:
                                chosenCard = c

                        #print('card played is:', chosenCard)
                        
                    else:

                        for c in listMySurvivors:
                            if (c.value + pegCount) != 5 and c.value != 5:
                                chosenCard = c

                        #print('card played is:', chosenCard)


                elif pegCount<=19:  #target a result of 16-20 before the opponent's next card

                    for c in listMySurvivors:
                        if c.value + pegCount >= 16 and c.value + pegCount <= 20 and c.value != 5:
                            chosenCard = c

                    #print('card played is:', chosenCard)

                elif pegCount<=30:     #maximize towards 31
                    #print('card played is:', chosenCard)
                    pass


##        print('Final Chosen Card is:', chosenCard)
##        print('Final Points Pegged is:', pointsPegged)

        return chosenCard, pointsPegged



        



        
            
    def pegSimulate(self,listMyHand,listOppHand,my_crib):
        """pegSimulate(listMyHand,listOppHand,my_crib): simulate a pegging session using the cards in my hand, the cards in the opponent's hand and my_crib to determine who goes first """
        myPoints=0
        oppPoints=0
        listPreviousCardsPlayed = []
        valuePegged = 0
        myTurn = not my_crib
        myActive = True
        oppActive = True

        #loopNum = 0

        while len(listMyHand)>0 or len(listOppHand)>0:
            #loopNum += 1
            #print('Loop number', loopNum, 'has started', 'myTurn is:', myTurn, 'I have cards:', len(listMyHand), 'opp has cards', len(listOppHand) )
            
            if myTurn:
                c1, points = self.pegDecision(listMyHand, listPreviousCardsPlayed)
                
                if c1 != None:
                    myPoints += points
                    valuePegged += c1.value
                    listPreviousCardsPlayed.append(c1)
                    listMyHand.remove(c1)

                    if len(listMyHand) == 0 and  len(listOppHand) == 0 and valuePegged < 31:
                        myPoints +=1

                    #print('card played:', c1, 'points scored', points, 'pegged value', valuePegged)
                else:
                    myActive = False
                    if not oppActive:
                        if valuePegged < 31:
                            myPoints += 1
                        listPreviousCardsPlayed.clear()
                        valuePegged = 0
                        myActive = True
                        oppActive = True
                    else:               #opponent still active
                        pass
                        
                myTurn = not myTurn
            else:
                c1, points = self.pegDecision(listOppHand, listPreviousCardsPlayed)
                
                if c1 != None:
                    oppPoints += points
                    valuePegged += c1.value
                    listPreviousCardsPlayed.append(c1)
                    listOppHand.remove(c1)

                    if len(listMyHand) == 0 and  len(listOppHand) == 0 and valuePegged < 31:
                        oppPoints +=1

                    #print('\t\t\t\t\t\t\tcard played:', c1, 'points scored', points, 'pegged value', valuePegged)
                else:
                    oppActive = False
                    if not myActive:
                        if valuePegged < 31:
                            oppPoints += 1
                        listPreviousCardsPlayed.clear()
                        valuePegged = 0
                        myActive = True
                        oppActive = True
                    else:               #I'm still active
                        pass
                        
                myTurn = not myTurn
                
            #print('Loop number', loopNum, 'has ended')
            
##        print('my points:', myPoints)
##        print('opp points', oppPoints)
##        print('net points', myPoints-oppPoints)
        return myPoints-oppPoints


    
    
class Deck:
    """Deck class: has properties ...   has methods ... """
    def __init__(self):
        """__init__(): initialize a deck of cards, all 52 cards in a list called cards """
        self.cards = []

        suits = ['c','d','h','s']
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        for s in suits:
            for r in ranks:
                self.cards.append( Card(r+s) )
       
        

        
if __name__ == '__main__':
    pass
##    Testing one 4-card hand with a deck card
##    h1 = Hand()                                   #instantiate Hand
##    h1.fillHand('5h','5s','Jh','5d')              #fillHand
##    p0 = h1.calcPoints('5h',True)                 #calcPoints
##    print(p0)


##    chaining example
##    p1 = h1.fillHand('5h','6h','7h','8h').calcPoints('9s',True)
##    p2 = h1.fillHand('5h','6h','7h','8h').calcPoints('9s',False)
##    p3 = h1.fillHand('5h','6h','7h','8s').calcPoints('9h',True)
##    print(p1)
##    print(p2)
##    print(p3)
    

##    Simulating 15 possible discard decisions
    f1 = FullHand('10h','10c','10s','Kh','Ks','Kc')
    f1.simulate(my_crib=False)



##how to use this module for a cribbage game

##how to decide which 2 cards to throw away
#import crib
#f1 = crib.FullHand('9c','6c','4d','5h','7d','8c')      #create a FullHand object with 6 cards dealt 
#discard1, discard2 = f1.simulate(True)                 #figure out which 2 cards to discard to maximize points
#print(discard1)                                        #optionally print the first card to discard
#print(discard2)                                        #optionally print the second card to discard

##how to decide which card to play during pegging
#import crib
#p1 = crib.Pegging()                                                                                                                            #create a Pegging object and assign to p1 
#cardToPlay, pointsPegged = p1.pegDecision( [crib.Card('Kc'),crib.Card('As'),crib.Card('10c')], [crib.Card('3s'),crib.Card('Ah')] )             #input cards in hand as first list, cards played thus far in order in the second list - assign card to play and points pegged to variables
#print(cardToPlay)                                                                                                                              #optionally print the card to play next in pegging
#print(pointsPegged)                                                                                                                            #optionally show how many points this would score

