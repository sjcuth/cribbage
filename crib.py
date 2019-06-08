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
    """Hand class: has properties cards, deckCard, allCards   has methods fillHand(card1,card2,card3,card4), calcPoints(deckCard)"""
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


    def calcPoints(self,deckCard):
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

        #calculate flush points
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


        

        
if __name__ == '__main__':
    h1 = Hand()                             #instantiate Hand
    h1.fillHand('5h','5s','Jh','5d')        #fillHand
    p0 = h1.calcPoints('5h')                #calcPoints
    print(p0)
    
    #chaining example
    p1 = h1.fillHand('5h','5s','Jh','5d').calcPoints('Jd')
    p2 = h1.fillHand('5h','5s','Jh','5d').calcPoints('Qs')
    p3 = h1.fillHand('5h','5s','Jh','5d').calcPoints('5h')
    print(p1)
    print(p2)
    print(p3)
    
