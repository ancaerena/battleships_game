from random import randint

def welcome_message():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the best Battleship game")
    print("Be ready to guess your opponent strategy in placing their ships on the board")
    print("The board size is 5, with 4 ships")
    print("For your guesses, please chose numbers between 0 and 4, for both columns and rows")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def get_player_name():
    """
    Get player's name to be used further in the game
    """
    player = input("Please enter your name:\n")



def main():
    welcome_message()
    get_player_name()

main()