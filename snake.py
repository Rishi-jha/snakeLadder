'''
Created on Sep 14, 2018

@author: Rishikesh Jha
'''
import random
import string
import sys
from collections import OrderedDict

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
    game = GameInit()
    game.start()
    c = input("Want to play Another Game??? (y/n): ")

