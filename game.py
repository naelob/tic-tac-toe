import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartPlayer

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.winner = " "
    
    @staticmethod
    def make_board():
        board = []
        for i in range(9):
            board.append(" ")
        return board

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    # shows the game board with number for first example
    def print_board_nums():
        number_array = [ [str(i) for i in range(j*3, (j+1)*3)] for j in range(3) ]
        for row in number_array:
            print('|' + '|'.join(row) + '|')

    # check if we can move to the square (if the square number is empty)
    def make_move(self, square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.success_game(square, letter):
                self.winner = letter
            return True
        return False  

    

    def success_game(self,square,letter):
        # horizontal test
        row_index = math.floor(square/3)
        # we fetch the row where the square is included
        row = self.board[row_index*3:(row_index+1)*3] 
        if all([s == letter for s in row]):
            return True
        
        # vertical test
        col_index = square%3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        # diagonal test
        if square%2 ==0:

            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    #check if there is still an empty square
    def empty_squares(self):
        return ' ' in self.board
    
    # we get the number of empty squares in the board
    def num_empty_squares(self):
        return self.board.count(' ')

    # we fetch the available moves possible in the game
    def available_moves(self):
        return [i for i,x in enumerate(self.board) if x==" "]
    
def play(game,x_player,o_player):
    
    game.print_board_nums()
    
    letter = 'X'

    while game.empty_squares():
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square,letter):

            print(letter + ' makes a move to square {}'.format(square))
            game.print_board()
            print('')
            
            # we check if there is a winner
            if game.winner != " ":
                print(letter+ ' HAS WON!')
                return  # we exit the game
            letter = 'O' if letter =='X' else 'X' # we switch the player turn
        time.sleep(.8)
    
    print('It\'s a tie!')
    
if __name__=='__main__':
    x_player = SmartPlayer('X')
    o_player = HumanPlayer('O')
    t=TicTacToe()
    play(t,x_player,o_player)

                

