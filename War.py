from random import shuffle

class Card:
    suits= ("spades","hearts","diamonds","clubs")
    values= ("None","None","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace")

    def __init__(self, v, s):
        self.value=v
        self.suit=s

    def __lt__(self,c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v= self.values[self.value]+" of "+self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(0,4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def remove(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()


class Player:
    def __init__(self,name):
        self.wins=0
        self.name=name
        self.card=None


class Game:
    def __init__(self):
        name1= input("Player 1 name:")
        name2= input("Player 2 name:")
        self.deck= Deck()
        self.p1= Player(name1)
        self.p2= Player(name2)

    def draw(self,p1c,p1n,p2c,p2n):
        d= "{} drew {}, {} drew {}."
        d= d.format(p1n,p1c,p2n,p2c)
        print(d)

    def wins(self, winner):
        w= "{} wins this round!"
        w= w.format(winner)
        print(w)
        print("\n","\n")

    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return ("War is over. "+p1.name+" wins!")
        if p1.wins<p2.wins:
            return ("War is over. "+p2.name+" wins!")
        return "It was a tie!"

    def play_game(self):
        cards=self.deck.cards
        print("Game Begins:","\n")
        while len(cards)>=2:
            m="Press 'q' to Quit! Any key to play:"
            ch= input(m)
            print("\n")
            if ch=='q':
                break
            p1c= self.deck.remove()
            p2c= self.deck.remove()
            p1n= self.p1.name
            p2n= self.p2.name
            self.draw(p1c,p1n,p2c,p2n)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)
        print(self.winner(self.p1,self.p2))


game= Game()
game.play_game()
                
        
            
