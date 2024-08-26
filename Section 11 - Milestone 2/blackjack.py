import random, unicodedata
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
at_table = True
#define wether we are letting the player hit. false upon standing
game_on = True
#player hitting, starts out true
hitting = True
#Dealer hitting
dealear_hitting = True
#false until the player busts
player_bust = False
#False until the dealer busts
dealer_bust = False

class Card:
    def __init__(self,suit,rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self) -> None:
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
class Chips:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def remove(self,amount):
        if self.balance < amount:
            print(f'Chips Unavailable.\nCurrent Balance:{self.balance}')
            return False
        else:
            self.balance -= amount
            print(f'Removed {amount} chips from {self.owner}. {self.owner} has {self.balance} chips remaining.')
            return amount
    
    def add(self,amount):
        self.balance += amount
        print(f'Added {amount} chips to {self.owner}. {self.owner} has {self.balance} chips remaining.')
        return amount
    
class Player(Chips):
    
    def __init__(self,name,total=100):
        Chips.__init__(self,name,total)
        self.name = name
        self.cards_in_play = []
        self.value = 0
        self.aces = 0

    def remove_one(self):
        return self.cards_in_play.pop(0)

    def add_cards(self,new_cards):
        self.cards_in_play.append(new_cards)
        self.value += values[new_cards.rank]
        
        #track aces
        if new_cards.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):

        while self.value >= 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        cards = []
        for num in range(len(self.cards_in_play)):
            cards.append(str(self.cards_in_play[num]))
        return ' | '.join(cards)

class Dealer(Chips):
        
        def __init__(self):
            self.name = 'House'
            Chips.__init__(self,self.name,0)
            self.cards_in_play = []
            self.value = 0
            self.aces = 0

        def remove_one(self):
            return self.cards_in_play.pop(0)

        def add_cards(self,new_cards):
            self.cards_in_play.append(new_cards)
            self.value += values[new_cards.rank]
        
        #track aces
            if new_cards.rank == 'Ace':
                self.aces += 1

        def adjust_for_aces(self):

            while self.value >= 21 and self.aces:
                self.value -= 10
                self.aces -= 1
        
        #using the dealers balance as a pot. It is zeroed out when the player loses.
        def payout(self):
            return self.balance*2

        def __str__(self):
            cards = []
            for num in range(len(self.cards_in_play)):
                cards.append(str(self.cards_in_play[num]))
            return ' | '.join(cards)

def digit_check(min,max,requestedNum):
    '''
    Re-Usable function to make sure a users input is a digit.
    Need to pass a minimum, maximum, and what the number you are requesting represents.
    '''
    choice = 'WRONG'
    acceptablerange = range(min,max)
    within_range = False

    #two conditions to check
    while choice.isdigit() == False or within_range == False:
        choice = input(f"Please enter a {requestedNum} ({min}-{max}): ")
        #digit check
        if choice.isdigit() == False:
            print('what you entered as not a digit.')

        if choice.isdigit() == True:
            if int(choice) in acceptablerange:
                within_range = True
            else:
                print('Please choose an acceptable amount of chips.')
                within_range = False
    
    return int(choice)

#TODO Write a function for taking bets
def take_bet(player,dealer):

    bet = digit_check(5,player.balance,'Bet')
    player.remove(bet)
    dealer.add(bet)
    
#Write a function for taking hits
def hit(player,deck):

    player.add_cards(deck.deal_one())
    player.adjust_for_aces()

#TODO write a function to allow the player to hit or stand
def hit_or_stand(player,deck):
    global hitting

    while True:
            h_Or_S = input('Would you like to hit or stand? Input h or s: ')

            if h_Or_S[0].lower() == 'h':
                hit(player,deck)
            elif h_Or_S[0].lower() == 's':
                print('Player Stands. Dealer is playing')
                hitting = False
            else:
                print('Sorry, please try again.')
                continue
            break

#Write a function to show all cards
def show_all(player,dealer):
    pvalue = 0
    dvalue = 0
    
    for card in player.cards_in_play:
        pvalue += card.value
    for card in dealer.cards_in_play:
        dvalue += card.value

    
    print(f"{dealer.name}'s Hand: ")
    print(dealer,' Value: {} Balance: {}'.format(dvalue,dealer.balance))
    print(f"{player.name}'s Hand: ")
    print(player,' Value: {} Balance: {}'.format(pvalue,player.balance))

#write a funciton to show some cards
def show_some(player,dealer):
    pvalue = 0
    dvalue = 0
    
    for card in player.cards_in_play:
        pvalue += card.value
    for card in dealer.cards_in_play:
        dvalue += card.value

    print(f"{dealer.name}'s Hand: ")
    print("Bicycle"," | ",dealer.cards_in_play[1])
    print(f"{player.name}'s Hand: ")
    print(player,f'Value: {pvalue}')

#Write functions to handle end game scenarios
#check after each hit
def player_busts(player,dealer):
    global game_on
    global hitting
    player.adjust_for_aces()
    if player.value > 21:
        print('Player Busts function executed')
        dealer.balance = 0
        game_on = False
        hitting = False
        return True
    else:
        return False

def player_wins(player,dealer):
    player.adjust_for_aces()
    dealer.adjust_for_aces()

    if player.value == 21 and dealer.value != 21:
        print('Player Wins!')
        player.add(dealer.payout())
        dealer.balance = 0
        return True
    elif player.value > dealer.value:
        print('Player wins!')
        player.add(dealer.payout())
        dealer.balance = 0
        return True
    else:
        return False

def dealer_busts(player,dealer):
    global dealear_hitting
    dealer.adjust_for_aces()
    if dealer.value > 21:
        player.add(dealer.payout())
        dealer.balance = 0
        dealear_hitting = False
        return True
    else:
        return False
    
def dealer_wins(player,dealer):
    global dealear_hitting
    player.adjust_for_aces()
    dealer.adjust_for_aces()

    if dealer.value == 21 and player.value != 21:
        print('Dealer Wins!')
        dealer.balance = 0
        return True
    elif player.value < dealer.value:
        print('Dealer wins!')
        dealer.balance = 0
        return True
    else:
        return False
    
def push(player,dealer):
    if player.value == dealer.value:
        print('Dealer and player tie push function')
        player.add(dealer.balance)
        dealer.balance = 0
        return True
    else:
        return False

def game_on_choice():
    choice = 'Wrong'
    while choice.lower() not in ['y','n']:
        choice = input('Keep Playing? (Y,N): ')

        if choice.lower() not in ['y','n']:
            print('sorry, invalid choice!')

    if choice.lower() == 'y':
        return True
    else:
        return False
#Game Setup

# Create the Player
player_name = input('Please enter your name: ')
human = Player(player_name)

# Create the computer
computer = Dealer()
# Create the deck
print(f'Welcome to blackjack {human.name}! You are starting with {human.balance}')
print(f'Your goal is to get as much money from the house as possible by beating the {computer.name}!')
print("Let's Play!")

while at_table:
    player_bust = False
    dealer_bust = False
    computer.value = 0
    human.value = 0
    hitting = True
    new_deck = Deck()

    #TODO Shuffle the Deck
    new_deck.shuffle()

    #Game Logic: Two possible actions, hit or stay.
    human.cards_in_play = []
    computer.cards_in_play = []
    for num in range(2):
        human.add_cards(new_deck.deal_one())
        computer.add_cards(new_deck.deal_one())


    
        
    show_some(human,computer)
    take_bet(human,computer)
    
    while hitting and not player_bust:
        print('\n')
        hit_or_stand(human,new_deck)
        show_some(human,computer)
        player_bust = player_busts(human,computer)

    while computer.value < 17 and not dealer_bust and not player_bust:
        hit(computer,new_deck)
        show_all(human,computer)

    if player_busts(human,computer):
        print("dealer wins by bust")
    elif dealer_busts(human,computer):
        print('player wins by bust')
    elif push(human,computer):
        print('push?')
    elif player_wins(human,computer):
        print('player wins by val')
    elif dealer_wins(human,computer):
        print('dealer wins by val')
    else:
        print('I got confused')
        
    
    show_all(human,computer)
    if human.balance < 5:
        print('you are out of money!')
        at_table = False
    else:
        at_table = game_on_choice()


#game ending: Player busts: player stays, computer wins: player stays, computer busts
#face cards are ten.
#ace is one or eleven.


#test take bet
#take_bet(Human,computer)