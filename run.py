# import module "random" from python library.
# This module provides functions to generate random numbers.
import random


while True:
    print("--------------------------------------------------")
    BOARD_SIZE = int(
        input("\nChose SIZE of the board (5-10)"))

    if 5 <= BOARD_SIZE <= 10:
        print(
            f"The SIZE of the Board is -> {BOARD_SIZE}")
        break
    else:
        print(
            "The SIZE of the board should be from: 5-10")


NUM_SHIPS = 3

SCORES = {"player": 0, "enemy": 0}


class Board:
    """
    Represents a Battleship game board.
    """

    def __init__(self, size=BOARD_SIZE):
        """
           Initialize the board with a given size and empty grid.
           The board grid containing symbols for water (~), ships (@),
           hits (X), and misses (O).
        """
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

        hide_ships (bool): If True, hides ships ("@") when displaying the board
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
        """Return True if all ships on this board have been sunk,
           otherwise False.
        """
        return all(self.grid[i][j] != "@" for i, j in self.ships)

    def attack(self, x, y, players):
        """
        Process an attack at the given coordinates.

        Args:
            x (int): Row coordinate.
            y (int): Column coordinate.

        Returns:
            str: "hit" if a ship is hit, "miss" if water is hit,
            "repeat" if already attacked.
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
    Represents a Battleship game between a player and the computer(Enemy).

    Attributes:
        player_board (Board): The board containing the player's ships.
        enemy_board (Board): The board containing the enemy's ships.
        turns (int): The number of turns taken in the game.
    """

    def __init__(self):
        """
            Initialize three instances. The instances self.player_board
            and self.enemy create each one, new instances of Board class.
            Board class create two boards and place ships for both player
            and enemy. And one more instance self.turns = 0 to reset the
            number of turns taken in the game.
        """
        self.player_board = Board()
        self.enemy_board = Board()
        self.turns = 0

        self.player_board.place_ships(NUM_SHIPS)
        self.enemy_board.place_ships(NUM_SHIPS)

    def score(self):
        """
        Return f'string type with the update Player vs Enemy score.
        """
        return f"PLAYER SCORE: {SCORES['player']}         ENEMY SCORE: {SCORES['enemy']}"

    def get_player_move(self):
        """
        Prompt the player to enter attack coordinates.

        Returns:
            tuple[int, int]: A valid (row, column) coordinate entered by the player.
        """
        while True:
            try:
                x = int(input(f"Enter row (0-{BOARD_SIZE - 1}): "))

                y = int(input(f"Enter column (0-{BOARD_SIZE - 1}): "))
                if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                    return x, y
                else:
                    print("Coordinates out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers.")

    def play(self):
        """
        Start and run the game loop until either the player or computer(enemy) wins,
        or until the game ends in a draw or the player quits.
        """
        print("\nWelcome to BattleShipe Game!\n")

        while True:
            # Shows how many turns left for the end of the match
            print(
                f"            |Round {self.turns + 1} of {BOARD_SIZE * BOARD_SIZE}|")
            print(f"{self.score()}\n")
            print(
                "\nYour Board (showing your ships(@) and enemy's attacks(x)):")
            self.player_board.print_board(hide_ships=False)
            print("\nEnemy's board (showing your attacks only):")
            self.enemy_board.print_board(hide_ships=True)

            # Player's turn
            print("\nYour turn to attack!\n")
            # Call the method of the class BattleshipGame and return a tuple(x,y)
            #  with the coordinates given by the player
            x, y = self.get_player_move()
            result = self.enemy_board.attack(x, y, "player")

            if result == "hit":

                print(f"You Hit computer's ship at ({x}, {y})")
                if self.enemy_board.all_ships_sunk():

                    print("You sank all the computer's ships! You win!")
                    break
            elif result == "miss":

                print(f"You MISS computer's ship at the coordinate ({x},{y}).")
            else:
                while result == "repeat":
                    print("You have already tried this position.")
                    x, y = self.get_player_move()
                    result = self.enemy_board.attack(x, y, "player")

            # Computer's (Enemy) turn
            print("\nEnemy's turn!\n")
            enemy_result = "repeat"

            while enemy_result == "repeat":  # Loop until it has a valid attack
                cx = random.randint(0, BOARD_SIZE - 1)
                cy = random.randint(0, BOARD_SIZE - 1)
                enemy_result = self.player_board.attack(cx, cy, "enemy")

            if enemy_result == "hit":
                print(f"The Enemy hits your ship at ({cx},{cy})!")
                if self.player_board.all_ships_sunk():
                    print("The Enemy sank all your ships! You lose!")
                    break
            elif enemy_result == "miss":
                print(
                    f"The Enemy MISS your ship at the coordinate ({cx},{cy}).")
            # Ask if player wants to continue
            continuar = input(
                "Do you want to continue (y/n) -> \n").lower()
            if continuar == 'n':
                print("You chose to quit the game. Goodbye!")
                break
            # Verify if the number of turns is greater than the total number of
            # coordinates in the board. If so, It finish the game as a draw.
            self.turns += 1
            if self.turns > BOARD_SIZE * BOARD_SIZE:
                print("It's a draw!")
                break


game = BattleshipGame()
game.play()
