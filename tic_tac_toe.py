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
        self.token_separator = '   '
        # initiates blank board
        self.board = [
                ['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']
                ]

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



def main():
    # Intro

    player1 = input(f'Player 1, please enter your name: ')
    player2 = input(f'Player 2, please enter your name: ')

    game = Game(Board(), Player(player1, 'X'), Player(player2, 'O'))

    print(f'Excellent, lets begin, {game.player1.name} and {game.player2.name}!')
    print("We'll take turns choosing moves.")
    print("When it's your turn, enter your move as a coordinate pair.")
    print('')
    print('Ex: "1, 2" puts a mark on the first row and second column, like so:')
    game.board.add_move(Move(game.player1,[0, 1]))
    game.board.display()
    print('')
    print("Let's start with a new board:")
    game.board = Board()

    current_player = game.player2

    while True:
        current_player = (game.player1 
                            if current_player == game.player2 
                            else game.player2)
        coord_of_move = input(f"What's your move, {current_player.name}? ")
        coord_of_move = coord_of_move.split(',')
        position = [int(num)-1 for num in coord_of_move]
        move = Move(current_player, position)
        game.board.add_move(move)
        game.board.display()

        












if __name__ == '__main__':
    main()


# # Create two players
# harry = Player('Harry', 'X')
# ron = Player('Ron', 'O')

# # Create game board
# the_board = Board()

# the_game = Game(the_board, harry1, ron)

# first_move = Move(harry,[0,2])

# the_board.add_move(first_move)

# the_board.display()









