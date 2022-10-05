from inspect import stack
import random


class ActionHandler():
    def __init__(self, hands):
        self.hands = hands
    def first_player(self):
        starting_player = random.randint(1, self.players)
        return starting_player

class Action(ActionHandler):
    def __init__(self, players, stack):
        self.players = players
        self.pot = 0
        self.action_stack = []
        self.bet_stack = 0
        self.actions = ['check','bet','call','raise','fold']
        self.stack = stack
    def check(self):
        self.action_stack = 'check'
        pass
    def bet(self, amount):
        self.pot += int(amount)
        return self.action_stack
    def round(self, previous_action):
        Action.action_stack = previous_action
        actions = self.actions
        if self.action_stack == 'check':
            actions = ['check', 'bet', 'fold']
        elif self.action_stack == 'bet':
            actions = ['call', 'raise', 'fold']
        elif self.action_stack == 'call':
            actions = ['call', 'raise', 'fold']
        elif self.action_stack == 'raise':
            actions = ['call', 'raise', 'fold']
        else:
            actions = ['check','bet','call','raise','fold']
        while True:       
            i = 1
            print("Player stack: " + str(self.stack))
            print("Pot: " + str(self.pot))
            for action in actions:
                print("{}. {}".format(i, action))
                i += 1
            response = input()
            # if player is a bot response = evalute
            if response == 'check' or response == '1':
                self.check()
                self.action_stack = 'check'
                self.bet_stack = 0
                break
            elif response == 'bet' or response == '2':
                amount = input('Enter Bet Amount:\n>>>')
                try:
                    if int(amount) > self.bet_stack and self.stack >= int(amount):
                        self.bet_stack = int(amount)
                        self.bet(amount)
                        self.stack -= int(amount)
                        break
                    else:
                        continue
                except:
                    pass
                    print("Enter a number")
            elif response == 'raise' or response == '3':
                amount = input('Enter Raise Amount. Previous bet/raise: ' + str(self.bet_stack))
                try:
                    if int(amount) > self.bet_stack and self.stack >= int(amount):
                        self.bet_stack = amount
                        self.bet(amount)
                        self.stack -= int(amount)
                        break
                    else:
                        continue
                except:
                    pass
            elif response == 'call' or response == '4':
                if self.stack >= self.bet_stack and self.stack != 0:
                    self.bet(self.bet_stack)
                    self.stack -= int(amount)
                    break
                else:
                    continue
            elif response == 'fold' or response == '5':
                pass

class Bot(Action):
    # sort player hand and board
    def evaluate(self, board, hand):
        # need player hand, board, rules

        pass
    def medium(self):
        # medium hand (2nd pair)
        # calls or bets small
        pass
    def strong(self):
        # strong hand
        # 25% of the time disguise, 75% bet or raise
        pass
    def weak(self):
        # weak semibluff (bottom pair, two overs)
        # 25% bluff strong 75 fold
        pass
    def weaker(self):
        # very weak
        # fold
        pass
    def nuts(self):
        # nuts
        # call, raise, shove river or turn
        pass