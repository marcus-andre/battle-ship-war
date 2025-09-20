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


