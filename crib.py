#add y = x[:] to copy arrays
#x[len(x):] = [5,6,7] to extend arrays
#x.remove(3) to remove a card

import random

"""crib module. Contains classes Card, Hand"""
class Card:
    """Card class: has properties strRank, strSuit, suitNum, rankNum, value, rankString, suitString   has method for print override"""
    def __init__(self,strDef):
        
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
        return self.rankString + ' of ' + self.suitString + ' - ' + self.strRank + self.strSuit + " - Suit Num: " + str(self.suitNum) + " Rank Num: " + str(self.rankNum) + " Point Value: " + str(self.value)
    
class Hand:
    """Hand class: has properties cards, deckCard, allCards   has methods fillHand(card1,card2,card3,card4), calcPoints(deckCard,is_crib)"""
    def __init__(self):
        self.cards = []

            
    def fillHand(self,card1,card2,card3,card4):

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
        self.deckCard = Card(deckCard)
        self.allCards = []
        for card in self.cards:
            self.allCards.append(card)
        self.allCards.append(self.deckCard)

        pointValue = 0

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
    """FullHand class: has properties ...   has methods ... """
    def __init__(self,card1,card2,card3,card4,card5,card6):
        
        self.fullHandCards = []

        self.fullHandCards.append( Card(card1) )
        self.fullHandCards.append( Card(card2) )
        self.fullHandCards.append( Card(card3) )
        self.fullHandCards.append( Card(card4) )
        self.fullHandCards.append( Card(card5) )
        self.fullHandCards.append( Card(card6) )

        
    def simulate(self,my_crib):

        crib_simulations = 2000
        h1 = Hand()
        h2 = Hand()
        x=0
        for discard1 in self.fullHandCards[x:5]:
            y=x+1
            for discard2 in self.fullHandCards[y:]:

                handCards = self.fullHandCards[:]
                handCards.remove(discard1)
                handCards.remove(discard2)

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
                simulation_number = 0
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

                        h2.fillHand( c2.strRank + c2.strSuit,c3.strRank + c3.strSuit,discard1.strRank + discard1.strSuit,discard2.strRank + discard2.strSuit )
                        cribsum += h2.calcPoints(c.strRank + c.strSuit, True)
                        cribcount+=1

                        simulation_number += 1

                avg_hand_points = round(psum / pcount,2)

                if my_crib:
                    avg_crib_points = round(cribsum / cribcount,2)
                else:
                    avg_crib_points = round(cribsum / cribcount,2) * -1
        
                
                print( "throwing away", discard1.strRank + discard1.strSuit, discard2.strRank + discard2.strSuit, "and keeping", handCards[0].strRank + handCards[0].strSuit,handCards[1].strRank + handCards[1].strSuit,handCards[2].strRank + handCards[2].strSuit,handCards[3].strRank + handCards[3].strSuit, "results in an average hand points of: ", avg_hand_points, "and average crib points of:", avg_crib_points, "for a total points of:", round(avg_hand_points + avg_crib_points,2) )

                #TODO: simulate crib hand

                #move this up to the 15x loop above
                #if my_crib:
                    #crib_points = 0
                    #15 possibilities for 2 cards in the crib
                    #simulate 46x45x44 (90000+) possibiities for the other 3 cards
                    #or fewer random simulations
                    #ccount = 0
                    #csum = 0
                
                #else:  #my_crib is false
                    #crib_points = 0


                #TODO: simulate peg +/-
                    #call the function for pegging with the correct arguments - put random cards in listOppHand - keep track of listPreviousCardsPlayed in class? 
                    #create Pegging object
                    #call pegSimulate()

                
            x+=1





#class Pegging:
#    """Pegging class: has properties ...   has methods ... """
#    def __init__(self):

        #self.listPreviousCardsPlayed = []
        #self.listMyHand = []
        #self.listOppHand = []
        #self.pegCount = 0

    #def pegDecision(self,listMyHand,listOppHand,listPreviousCardsPlayed):
            #pegCount = 0
            #for c in previousCardsPlayed:
                #pegCount+=c.value

            #del infeasible cards from both hands

            #make decision
            #evaluate decision for 15, pair, run - choose it
            #otherwise if low keep below 5 or above 15 #if high push as high towards 51

            #add card to listPreviousCardsPlayed

            #return card that is played
            
    #def pegSimulate(self,listMyHand,listOppHand,listPreviousCardsPlayed):
        #myPoints=0
        #oppPoints=0

        #loop while players have cards
            #call pegDecision()

        #return myPoints-oppPoints


    
class Deck:
    """Deck class: has properties ...   has methods ... """
    def __init__(self):
        
        self.cards = []

        suits = ['c','d','h','s']
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        for s in suits:
            for r in ranks:
                self.cards.append( Card(r+s) )
       
        

        
if __name__ == '__main__':
##    Testing one 4-card hand with a deck card
##    h1 = Hand()                                   #instantiate Hand
##    h1.fillHand('5h','5s','Jh','5d')              #fillHand
##    p0 = h1.calcPoints('5h',True)                 #calcPoints
##    print(p0)
##    
    #chaining example
##    p1 = h1.fillHand('5h','6h','7h','8h').calcPoints('9s',True)
##    p2 = h1.fillHand('5h','6h','7h','8h').calcPoints('9s',False)
##    p3 = h1.fillHand('5h','6h','7h','8s').calcPoints('9h',True)
##    print(p1)
##    print(p2)
##    print(p3)
    

##    Simulating 15 possible discard decisions
    
    f1 = FullHand('10s','9d','8d','7s','6c','5h')
    f1.simulate(False)
    
##>>> import crib
##>>> f1 = crib.FullHand('5s','6d','10d','7s','9c','8h')
##>>> f1.simulate(True)







































