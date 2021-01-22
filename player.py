import math
import random

#super class for player
class Player():
    def __init__(self,letter):
        self.letter = letter

    def get_move(self,game):
        pass

#class for the human player
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # we get the number of square of the player
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square: # we still stay here while the user choose a valid square number
            square = input(self.letter + '\'s turn. Input move (0-9): ') # we ask the player an input number 
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square =True
            except ValueError:
                    print('Please choose a valid input.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        val = random.choice(game.available_moves)
        return val


class SmartPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # if we havent played yet, we choose a random square number
        if(len(game.available_moves())==9): 
            square = random.choice(game.available_moves())
        # else we use the minimax function to choose the best square in order to increase the computer's chances of winning. 
        else:
            square = self.minimax(game,self.letter)['position']
        return square

    def minimax(self,state,player):
        max_player = self.letter # ourselves

        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move
    
            # undo move
            state.board[possible_move] = ' '
            state.winner = " "
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best