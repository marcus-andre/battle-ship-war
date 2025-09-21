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

