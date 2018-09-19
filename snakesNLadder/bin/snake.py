'''
Created on Sep 14, 2018

@author: Rishikesh Jha
'''
import random
import string
import sys
from collections import OrderedDict

PLAYER_TURN_END = 0
PLAYER_WON = 1
BOUNDRIES_EQ = "=" * 40 
BOUNDRIES_HP = "-" * 40
DICE = [i for i in range(1,7)]
board = {1: 1, 2: 38, 3: 3, 4: 4, 5: 5, 6: 6, 7: 14, 8: 31, 9: 9, 10: 10,
         11: 11, 12: 12, 13: 13, 14: 14, 15: 26, 16: 6, 17: 17, 18: 18, 19: 19,
         20: 20, 21: 42, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 84,
         29: 29, 30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 44, 37: 37,
         38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45, 46: 25,
         47: 47, 48: 48, 49: 11, 50: 50, 51: 67, 52: 52, 53: 53, 54: 54, 55: 55,
         56: 56, 57: 57, 58: 58, 59: 59, 60: 60, 61: 61, 62: 19, 63: 63, 64: 60,
         65: 65, 66: 66, 67: 67, 68: 68, 69: 69, 70: 70, 71: 91, 72: 72, 73: 73,
         74: 53, 75: 75, 76: 76, 77: 77, 78: 98, 79: 79, 80: 80, 81: 81, 82: 82,
         83: 83, 84: 84, 85: 85, 86: 86, 87: 94, 88: 88, 89: 68, 90: 90, 91: 91,
         92: 88, 93: 93, 94: 94, 95: 75, 96: 96, 97: 97, 98: 98, 99: 80, 100: 100}


class Player(object):
    '''
    Player class to create players
    '''

    def __init__(self, name=None, color=None, game_mode=1):
        '''
        :param: TODO
        '''
        self.name = name or "User_{0}".format(''.join(random.choices(string.ascii_uppercase + string.digits, k=6)))
        self.color = COLORS.pop(COLORS.index(random.choice(COLORS))) if COLORS else "COLOR_{0}".format(''.join(random.choices(string.ascii_uppercase , k=6)))
        self.current_position = 0
        self.current_die_value = None
        self.game_mode = game_mode
        self.move_count = 0
        self.rank = None

    def move(self):
        self.roll_dice()
        print("Your Dice: {}".format(self.current_die_value))
        self.move_to_next_position()
        self.move_count += 1
        if self.is_winner:
            return PLAYER_WON

        if self.game_mode != 1:
            if all([True if i==self.current_die_value[0] else False for i in self.current_die_value]):
                self.move()
        return PLAYER_TURN_END

    def roll_dice(self):
        self.current_die_value = [random.choice(DICE) for i in range(self.game_mode)]

    @property
    def is_winner(self):
        return self.current_position == 100

    def move_to_next_position(self):
        if self.current_position + sum(self.current_die_value) <= 99:
            self.current_position = board[self.current_position + sum(self.current_die_value)]
        else:
            self.current_position = board[2*100 - self.current_position - sum(self.current_die_value)]

class SnakeLaddersGame(object):

    def __init__(self, players):
        self.players = players

    def gameplay(self):
        _achieved_rank = 0
        players = self.players.copy()
        players_won = []
        while len(players) > 1:
            for player in players:
                rc = player.move()
                if rc == PLAYER_WON:
                    print("Player {} won!!!!\nCongrats.".format(player.name))
                    print("Rank: {}".format(_achieved_rank+1))
                    player.rank = _achieved_rank + 1
                    _achieved_rank += 1
                    players_won.append(players.pop(players.index(player)))
                    break
        players[0].rank = _achieved_rank + 1
        players_won.append(players[0])
        self._log_stats(players_won)

    def _log_stats(self, players):
        for player in players:
            self._log_player_stats(player)

    def _log_player_stats(self, player):
        text = OrderedDict([("Name", player.name),
                            ("Total Moves Taken", player.move_count),
                            ("Rank", player.rank)])
        print(BOUNDRIES_HP)
        print('\n'.join(['{0}: {1}'.format(k,v) for k,v in text.items()]))
        print(BOUNDRIES_HP)
        print('\n\n')


class GameInit(object):

    def __init__(self):
        self.players = []

    def start(self):
        self.load_initial_stuffs()
        self.load_players()
        self.play_game()

    def load_initial_stuffs(self):
        pass

    def load_game(self):
        return SnakeLaddersGame(self.players)
    def play_game(self):
        game_instance = self.load_game()
        game_instance.gameplay()
        

    def load_players(self):
        players_count = int(input("Select how many players( > 1 ): "))
        game_mode = int(input("Select number of die(1 or 2): "))
        print(BOUNDRIES_EQ)
        print("Creating Players: ")
        i = 1
        for pl in range(players_count):
            print("Player {0} details: ".format(i))
            player_name = input("Player Name (Enter for default): ")
            player_color = input("Player Color (Enter for default): ")
            self.players.append(Player(name=player_name, color=player_color, game_mode=game_mode))
            i += 1
c = 'y'
while c == 'y':
    COLORS = ["RED", "GREEN", "BLUE", "YELLOW"]
    game = GameInit()
    game.start()
    c = input("Want to play Another Game??? (y/n): ")

