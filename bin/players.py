'''
This module is a part of Snakes n Ladder Game.
This module will provide an Player object and associated functionalities with the player.

#########################################################################################
#                                                                                       #
#                       
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                 @author: Rishikesh Jha                                #
#                             @email: rishijha424@gmail.com                             #
#########################################################################################


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

COLORS = ["RED", "GREEN", "BLUE", "YELLOW"]


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
        self.symbol = None
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

    def mark_symbol(self, symbol):
      self.symbol = symbol

    @property
    def is_winner(self):
        return self.current_position == 100

    def move_to_next_position(self):
        if self.current_position + sum(self.current_die_value) <= 99:
            self.current_position = board[self.current_position + sum(self.current_die_value)]
        else:
            self.current_position = board[2*100 - self.current_position - sum(self.current_die_value)]
