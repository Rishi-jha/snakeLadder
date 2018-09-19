'''
This module is a part of Snakes n Ladder Game.
This module will provide the playing interface for the snake and Ladder Game.

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
from __future__ import print_function, unicode_literals
from snakesNLadder.lib import gameplay
from snakesNLadder.resources import licence, rules, bugs_suggestions
import sys
from PyInquirer import prompt
import os
from snakesNLadder.lib.style import QUESTIONS_MAIN_MENU, style


class SnakeLadder(object):

    def __init__(self):
        self.players = []
        self.gameplay = None
        self.answers = None

    def play(self):
        #self.load_game_introduction()
        self.load_menu()
        if self.answers["game_options"] == 0:
            sys.exit()
        elif self.answers["game_options"] == 2:
            self.show_licence()
        elif self.answers["game_options"] == 3:
            self.show_rules()
        elif self.answers["game_options"] == 4:
            self.show_feedback_text()
        elif self.answers["game_options"] == 1 and self.answers["game_mode"] != -1 and self.answers["dice_mode"] != -1:
            self.start_gameplay()
        os.system("clear")
        self.play()

    def load_game_introduction(self):
        print("into")

    def load_menu(self):

        self.answers = prompt(QUESTIONS_MAIN_MENU, style=style)

    @staticmethod
    def show_licence():
        licence.show()

    @staticmethod
    def show_rules():
        rules.show()

    @staticmethod
    def show_feedback_text():
        bugs_suggestions.show()

    def start_gameplay(self):
        gameplay.start(self.answers)

def start_game():
    game = SnakeLadder()
    game.play()

if __name__ == '__main__':
    start_game()