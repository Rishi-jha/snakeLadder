'''
Created on Sep 19, 2018

@author: Rishi
'''
from snakesNLadder.lib import gameboard, player
from snakesNLadder.lib.player import PLAYER_WON, BOUNDRIES_HP
from collections import OrderedDict
from PyInquirer import prompt
import sys

class BaseGamePlay(object):
    '''
    Base GamePlay Object to be served as base class for Single and Multiplayer GamePlay
    '''
    _NUMBER_OF_ACTUAL_PLAYERS = NotImplemented

    def __init__(self, answers):
        self.players = []
        self._NUMBER_OF_ACTUAL_PLAYERS = answers["no_of_players"]
        self.game_mode = answers["dice_mode"]
        print(self.game_mode)
        self.board = None

    def load_board(self):
        self.board = gameboard.load_board(self.players)

    def load_players(self):
        for player_id in range(self._NUMBER_OF_ACTUAL_PLAYERS):
            name = input("Enter the Player {0} Name: ".format(player_id + 1))
            self.players.append(player.Player(name, game_mode=self.game_mode))

    def start_play(self):
        self.load_players()
        self.load_board()
        self.gameplay()
        q = input("Want to Play Again? Y/N")
        if q == 'y':
            return
        sys.exit()

    def gameplay(self):
        _achieved_rank = 0
        players = self.players.copy()
        players_won = []
        while len(players) > 1:
            for player in players:
                self.each_move_prompt(player)
                rc = player.move()
                self.board_move(player)
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

    def each_move_prompt(self, player):
        prompt(player.get_next_move_question())

    def board_move(self, player):
        self.board.move(player)

def start(a):
    gameplay = BaseGamePlay(a)
    gameplay.start_play()