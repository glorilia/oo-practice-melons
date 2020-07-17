class Player():
    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece


class Move():
    def __init__(self, author, position):
        self.author = author
        self.position = position


class Board():

    def __init__(self):
        # Will keep archive of all moves
        self.moves = []
        # initiates blank board
        self.board = [
                ['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']
                ]
        self.token_separator = '   '

    def display(self):
        # Prints out contents of board row by row
        for row in self.board:
            # Each row is a list; join the strings with the token seperator
            print(self.token_separator.join(row))

              
        

    def add_move(self, move):
        # not sure about this either
        self.moves.append(move)
        self.board[move.position[0]][move.position[1]] = move.author.game_piece


class Game():
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = 'start'
        self.finished_at = 'end'

# Create two players
harry = Player('Harry', 'X')
ron = Player('Ron', 'O')

# Create game board
the_board = Board()

# the_game = Game(the_board, harry1, ron)

# first_move = Move(harry,[0,2])

# the_board.add_move(first_move)

# the_board.display()









