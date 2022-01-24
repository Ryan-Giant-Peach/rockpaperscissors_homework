from models.player import *

class Game():
    def __init__(self):
        self.the_winner = {
            "scissors": "paper",
            "paper": "rock",
            "rock": "scissors"
        }

    def play(self, player_1, player_2):

        winner = None

        if self.the_winner[player_1.choice.lower()] == player_2.choice.lower():

            winner = player_1
        elif self.the_winner[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2

        return winner


