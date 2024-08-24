'''
Python program that plays the card game war.
'''
import random

#Define Globals
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Card Class (Suit, rank, value)
class Card:
    def __init__(self,suit,rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit

#Deck Class

class Deck:
    def __init__(self) -> None:
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#TODO Player Class
class Player:
    
    def __init__(self,name) -> None:

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} Cards.'
# Test zone
new_deck = Deck()
new_deck.shuffle()
for card_object in new_deck.all_cards:
    print(card_object)

mycard = new_deck.deal_one()

print(mycard)
new_player = Player('Jose')
print(new_player)
new_player.add_cards([mycard,mycard,mycard])
print(new_player)
print(new_player.all_cards[0])