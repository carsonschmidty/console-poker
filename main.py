import random
import os

# clears console
def clear():
    os.system('cls')

# unfinished player class to handle player behaviour, betting, folding, etc
class Player():
    def __init__(self, money):
        self.money = money
        self.behaviour = None

    def sort_hands(self, hands, players):
        player_hands = {}
        for x in range(players):
            player_hands["player " + str(1+x)] = [hands[0+x],hands[players+x]]
        return player_hands

# instantiates a new game, called to progress rounds etc, has print capabilities
class Table():
    def __init__(self, players):
        self.players = players
    # shuffle deck, remove items from deck and insert them into the playing hands
    def shuffle(self, deck):
        self.deck = deck
        hands = []
        random.shuffle(deck)
        for x in range(2*self.players):
            self.deck.pop(x)
            hands.append(deck[x])
        self.hands = hands
        return hands
    # prints player hand
    def print_hand(self):
        player_hand = [self.hands[0],self.hands[self.players]]
        for card in self.hands:
            value = card[0]
            if value == 1:
                card[0] = 'A'
            elif value == 10:
                card[0] = 'T'
            elif value == 11:
                card[0] = 'J'
            elif value == 12:
                card[0] = 'Q'
            elif value == 13:
                card[0] = 'K'
        print("""
            ┌────────┐ ┌────────┐
            │      %s │ │      %s │
            │   %s    │ │   %s    │
            │        │ │        │
            │        │ │        │
            └────────┘ └────────┘
            """ % (player_hand[0][1], player_hand[1][1], player_hand[0][0], player_hand[1][0]))
    def flop(self):
        self.board=[]
        random.shuffle(self.deck)
        for x in range(3):
            self.board.append(self.deck[x])
        for card in self.board:
            value = card[0]
            if value == 1:
                card[0] = 'A'
            elif value == 10:
                card[0] = 'T'
            elif value == 11:
                card[0] = 'J'
            elif value == 12:
                card[0] = 'Q'
            elif value == 13:
                card[0] = 'K'
        print("""
            ┌────────┐ ┌────────┐ ┌────────┐
            │      %s │ │      %s │ │      %s │
            │   %s    │ │   %s    │ │   %s    │
            │        │ │        │ │        │
            │        │ │        │ │        │
            └────────┘ └────────┘ └────────┘ 
        """ % (self.board[0][1], self.board[1][1], self.board[2][1], self.board[0][0], self.board[1][0], self.board[2][0]))
    def turn(self):
        self.turncard = self.board
        random.shuffle(self.deck)
        self.turncard.append(self.deck[3])
        for card in self.turncard:
            value = card[0]
            if value == 1:
                card[0] = 'A'
            elif value == 10:
                card[0] = 'T'
            elif value == 11:
                card[0] = 'J'
            elif value == 12:
                card[0] = 'Q'
            elif value == 13:
                card[0] = 'K'
        print("""
            ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
            │      %s │ │      %s │ │      %s │ │      %s │
            │   %s    │ │   %s    │ │   %s    │ │   %s    │
            │        │ │        │ │        │ │        │
            │        │ │        │ │        │ │        │
            └────────┘ └────────┘ └────────┘ └────────┘
        """ % (self.turncard[0][1], self.turncard[1][1], self.turncard[2][1], self.turncard[3][1], self.turncard[0][0], self.turncard[1][0], self.turncard[2][0], self.turncard[3][0]))
    def river(self):
        self.rivercard = self.turncard
        random.shuffle(self.deck)
        self.rivercard.append(self.deck[4])
        for card in self.rivercard:
            value = card[0]
            if value == 1:
                card[0] = 'A'
            elif value == 10:
                card[0] = 'T'
            elif value == 11:
                card[0] = 'J'
            elif value == 12:
                card[0] = 'Q'
            elif value == 13:
                card[0] = 'K'
        print("""
            ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
            │      %s │ │      %s │ │      %s │ │      %s │ │      %s │
            │   %s    │ │   %s    │ │   %s    │ │   %s    │ │   %s    │
            │        │ │        │ │        │ │        │ │        │
            │        │ │        │ │        │ │        │ │        │
            └────────┘ └────────┘ └────────┘ └────────┘ └────────┘
        """ % (self.rivercard[0][1], self.rivercard[1][1], self.rivercard[2][1], self.rivercard[3][1], self.rivercard[4][1],self.rivercard[0][0], self.rivercard[1][0], self.rivercard[2][0], self.rivercard[3][0], self.rivercard[4][0]))  
    def deal(self):
        # player_hand = [card for card in self.hands if self.hands.index(card) == 0 or self.players]
        player_hand = []
        for card in self.hands:
            if self.hands.index(card) == 0 or self.hands.index(card) == self.players:
                player_hand.append(card)
        return player_hand
    def win(self):
        # compare river to eeach individual hand
        pass

def main():
    # create deck
    colors = ['♥','♦','♠','♣']
    deck = [[value, color] for value in range(1,14) for color in colors]
    # instantiate game with player count
    new_table = Table(4)
    # create hands
    new_table.shuffle(deck)

    player_hand = new_table.deal()
    print(player_hand)
    new_table.print_hand()
    new_table.flop()
    new_table.turn()
    new_table.river()


main()

