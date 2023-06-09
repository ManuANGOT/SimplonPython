# Autre méthode avec utilisation d'une classe et d'une bibliothèque (range)

import random

# Creation of a "Morpionibus" class, which will be the name of my game
class Morpionibus:

    def __init__(self):
        self.board = []


# Create the 3 x 3 board
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, joueur):
        self.board[row][col] = joueur

    def is_player_win(self, joueur):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != joueur:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != joueur:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != joueur:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != joueur:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, joueur):
        return 'X' if joueur == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        joueur = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {joueur} turn")

            self.show_board()

            # User input
            row, col = list(
                map(int, input("Enter a row number and a column number to validate your turn: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, joueur)

            # checking if current player is won or not
            if self.is_player_win(joueur):
                print(f"Player {joueur} wins the game!")
                break

            # checking if the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # pass the turn
            player = self.swap_player_turn(joueur)

        # display the board at the end of the game
        print()
        self.show_board()

# Starting
morpion = Morpionibus()
morpion.start()