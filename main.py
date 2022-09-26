import random
import os
from operator import itemgetter

# clears console
def clear():
    os.system('cls')

class World:
    def __init__(self, behavior, players, colors):
        self.behavior = behavior
        self.players = players
        pass

# unfinished player class to handle player behaviour, betting, folding, etc
class Player(World):
    def __init__(self, money):
        self.money = money
    # algorithmically sorts hands into a dictionary of each player



# instantiates a new game, called to progress rounds etc, has print capabilities
class Table():
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
    # shuffle deck, remove items from deck and insert them into the playing hands
    def shuffle(self):
        hands = []
        random.shuffle(self.deck)
        for x in range(2*self.players):
            self.deck.pop(x)
            hands.append(self.deck[x])
        self.hands = hands
        return hands
    def sort_hands(self):
        player_hands = {}
        for x in range(self.players):
            player_hands["player " + str(1+x)] = [self.hands[0+x],self.hands[self.players+x]]
        self.player_hands = player_hands
    # prints player hand
    def print_hand(self):
        cards = self.player_hands["player 1"]
        for card in cards:
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
            """ % (cards[0][1], cards[1][1], cards[0][0], cards[1][0]))
    def flop(self):
        self.board=[]
        random.shuffle(self.deck)
        for x in range(3):
            self.board.append(self.deck[x])
            self.deck.pop(x)
 
        cards = self.board
        for card in cards:
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
        """ % (cards[0][1], cards[1][1], cards[2][1], cards[0][0], cards[1][0], cards[2][0]))
    def turn(self):
        self.turncard = self.board
        random.shuffle(self.deck)
        self.turncard.append(self.deck[0])
        self.deck.pop(0)
        cards = self.turncard
        for card in cards:
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
        """ % (cards[0][1], cards[1][1], cards[2][1], cards[3][1], cards[0][0], cards[1][0], cards[2][0], cards[3][0]))
    def river(self):
        self.rivercard = self.turncard
        random.shuffle(self.deck)
        self.turncard.append(self.deck[0])
        self.deck.pop(0)
        cards = self.rivercard
        for card in cards:
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
        """ % (cards[0][1], cards[1][1], cards[2][1], cards[3][1], cards[4][1],cards[0][0], cards[1][0], cards[2][0], cards[3][0], cards[4][0]))  
        self.board = self.rivercard

    def player_score(self):
        # compare self.board to each players hand
        players_score = {}
        # find high card
        for key in self.player_hands:
            score = {
                'hand' : None,
                'high' : None,
                'pair' : None,
                'three' : None,
                'straight' : None,
                'flush' : None,
                'quad' : None,
                'full' : None,
                'str_flush' : None,
                'royal' : None
            }
            player_board = self.board
            #p1 cards
            cards = self.player_hands[key]
            score['hand'] = cards
            #add players cards to board
            player_board.append(cards[0])
            player_board.append(cards[1])
            #sort player board
            for card in player_board:
                value = card[0]
                if value == 'A':
                    card[0] = 1
                elif value == 'T':
                    card[0] = 10
                elif value == 'J':
                    card[0] = 11
                elif value == 'Q':
                    card[0] = 12
                elif value == 'K':
                    card[0] = 13
            sorted_player_board = sorted(player_board, key=itemgetter(0), reverse=False)
            #get high card
            score['high'] = sorted_player_board[len(player_board)-1][0]
            for cards in sorted_player_board:
                if cards[0] == 1:
                    score['high'] = 1
            #get pair
            for x in range(len(sorted_player_board)):
                try:
                    if sorted_player_board[x][0] == sorted_player_board[x+1][0]:
                        score['pair'] = sorted_player_board[x][0]
                        if sorted_player_board[x][0] == 1:
                            score['pair'] = sorted_player_board[x][0]
                            break
                except:
                    pass
            #get trip
            for x in range(len(sorted_player_board)):
                try:
                    if sorted_player_board[x][0] == sorted_player_board[x+1][0] and sorted_player_board[x][0] == sorted_player_board[x+2][0]:
                        score['three'] = sorted_player_board[x][0]
                        if sorted_player_board[x][0] == 1:
                            score['three'] = sorted_player_board[x][0]
                            break
                except:
                    pass    

            # flush
            colors = ['♥','♦','♠','♣']
            suits = []
            for x in range(len(sorted_player_board)):
                suits.append(sorted_player_board[x][1])
            for i in range(4):
                suit_count = suits.count(colors[i])
                if suit_count >= 5:
                    for card in sorted_player_board:
                        if card[1] == colors[i]:
                            score['flush'] = [[card[0]],[colors[i]]]
                    if sorted_player_board[0][0] == 1:
                        score['flush'] = [1,[colors[i]]] 
                    break

            #get straight
            straight_board = []
            for x in sorted_player_board:
                if x[0] not in straight_board:
                    straight_board.append(x[0])
            for x in straight_board:
                if x == 1:
                    straight_board.append(x)
                    break
            for x in range(len(straight_board)):
                try:
                    if straight_board[x] + 1 == straight_board[x+1]:
                        if straight_board[x+1] + 1 == straight_board[x+2]:
                            if straight_board[x+2] + 1 == straight_board[x+3]:
                                if straight_board[x+3] + 1 == straight_board[x+4]:
                                    score['straight'] = straight_board[x+4]
                                elif straight_board[x+3] == 13 and straight_board[0] == 1:
                                    score['straight'] = 1
                                    if score['flush'] != None:
                                        score['royal'] = True
                                elif straight_board[x] == 1:
                                    score['straight'] = 1
                except:
                    pass

            # full house, check if score['pair'] and score['three'] are filled, if so full house of trips
            if score['pair'] != None and score['three'] != None:
                if score['pair'] != score['three']:
                    score['full'] = score['three']
            # quad same logic as pair and threes
            for x in range(len(sorted_player_board)):
                try:
                    if sorted_player_board[x][0] == sorted_player_board[x+1][0] and sorted_player_board[x][0] == sorted_player_board[x+2][0] and sorted_player_board[x][0] == sorted_player_board[x+3][0]:
                        score['quad'] = sorted_player_board[x][0]
                        if sorted_player_board[x][0] == 1:
                            score['quad'] = sorted_player_board[x][0]
                            break
                except:
                    pass    
            # straight flush
            if score['straight'] != None and score['flush'] != None:
                score['str_flush'] = score['straight']
            # royal flush
            
            # print(score)
            players_score[key] = score
            player_board.pop(6)
            player_board.pop(5)

def main():
    colors = ['♥','♦','♠','♣']
    deck = [[value, color] for value in range(1,14) for color in colors]

    world = World(None, 4, colors)
    # instantiate game with player count
    new_table = Table(world.players, deck)
    # create hands
    new_table.shuffle()
    new_table.sort_hands()

    new_table.flop()
    new_table.turn()
    new_table.river()

    new_table.player_score()

main()

