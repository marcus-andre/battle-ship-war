#import module "random" from python library. This module provides functions to generate random numbers.
import random


while True:
    BOARD_SIZE = int(input("\nChose the \033[31mSIZE\033[0m of the board from \033[31m5-10\033[0m: "))
    if 5 <= BOARD_SIZE <= 10:
        print("\n---------------------------------------")
        print(f"The \033[31mSIZE\033[0m of the Board is \033[31m{BOARD_SIZE}\033[0m:")
        print("---------------------------------------")
        break
    else:
        print("---------------------------------------")
        print("The \033[31mSIZE\033[0m of the board should be from \033[31m5-10\033[0m:")
        print("---------------------------------------")


NUM_SHIPS = 3
SCORES = {"player": 0, "computer": 0}

class Board:
    """
    Represents a Battleship game board.

    """

    def __init__(self, size=BOARD_SIZE):
        """Initialize the board with a given size and empty grid."""
        self.size = size
        self.grid = [["~"] * size for _ in range(size)]
        self.ships = []

    def place_ships(self, num_ships=NUM_SHIPS):
        """
        Randomly place a specified number of ships on the board.
        Ships are represented by "@" on the grid.
        """
        while len(self.ships) < num_ships:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.grid[x][y] == "~":
                self.grid[x][y] = "@"
                self.ships.append((x, y))

    def print_board(self, hide_ships=False):
        """
        Print the board to the console.

        Args:
            hide_ships (bool): If True, hides ships ("@") when displaying the board.
        """
        print("  " + " ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.grid):
            display_row = []
            for cell in row:
                if hide_ships and cell == "@":
                    display_row.append("~")
                else:
                    display_row.append(cell)
            print(str(idx) + " " + " ".join(display_row))

    def all_ships_sunk(self):
        """Return True if all ships on this board have been sunk, otherwise False."""
        return all(self.grid[i][j] != "@" for i, j in self.ships)

    def attack(self, x, y, players):
        """
        Process an attack at the given coordinates.

        Args:
            x (int): Row coordinate.
            y (int): Column coordinate.

        Returns:
            str: "hit" if a ship is hit, "miss" if water is hit, "repeat" if already attacked.
        """
        if self.grid[x][y] == "@":
            self.grid[x][y] = "X"
            SCORES[players] += 1
            return "hit"
        elif self.grid[x][y] == "~":
            self.grid[x][y] = "O"
            return "miss"
        else:
            return "repeat"




class BattleshipGame:
    """
    Represents a Battleship game between a player and the computer.

    Attributes:
        player_board (Board): The board containing the player's ships.
        computer_board (Board): The board containing the computer's ships.
        turns (int): The number of turns taken in the game.
    """
    def __init__(self):
        """
            Initialize three instances, self.player_board and self.computer_board calling function Board.
            They create two boards and place ships for both player and computer. And one more instance 
            self.turns = 0 to reset the number of turns taken in the game.
        """
        self.player_board = Board()
        self.computer_board = Board()
        self.turns = 0

        self.player_board.place_ships(NUM_SHIPS)
        self.computer_board.place_ships(NUM_SHIPS)
        
    def score(self):
        """
        Return f'string type with the update Player vs Computer score. 
        """
        return f"PLAYER SCORE {SCORES['player']}         COMPUTER SCORE {SCORES['computer']}"
    







game = BattleshipGame()