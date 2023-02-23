import random
import time


def play_game():
    # a dictionary containing the game options
    game_options = {1: "Rock", 2: "Paper", 3: "Scissors"}

    # prompt user for their choice
    print("Your choices are:\n1. Rock\n2. Paper\n3. Scissors\n")
    choice = input("Choose a number! ")

    # check if user's input is valid, return if not
    if choice not in ['1', '2', '3']:
        print("Invalid input. Please choose 1, 2, or 3.")
        return play_game()

    # convert user's input to integer, then get corresponding choice name from dictionary
    choice = int(choice)
    choice_name = game_options[choice]
    print("You chose:", choice_name)
    time.sleep(1)

    # generate computer's choice and get corresponding choice name from dictionary
    comp_choice = random.randint(1, 3)
    comp_choice_name = game_options[comp_choice]
    print("I chose:", comp_choice_name)
    time.sleep(2)

    # determine the winner or if it's a tie, and set result accordingly
    if choice == comp_choice:
        result = "Draw"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = comp_choice_name
    else:
        result = choice_name

    # print the winner
    if result == choice_name:
        print()
        print()
        print("CONGRATULATIONS! YOU WIN!")
        return "win"
    elif result == "Draw":
        print()
        print()
        print("WE TIED!")
        return "tie"
    else:
        print()
        print()
        print("I WIN!")
        return "loss"


player_wins = 0
computer_wins = 0

while True:
    # play one round of the game
    result = play_game()
    if result == "win":
        player_wins += 1
    elif result == "loss":
        computer_wins += 1

    # print the current score
    print(f"Player: {player_wins} - Computer: {computer_wins}\n")

    # ask user if they want to play again, exit if not
    ans = input("Play Again? (Y/N) ")

    while ans.lower() not in ['y', 'n', 'yes', 'no']:
        ans = input("Invalid input. Please enter 'Y' or 'N': ")

    if ans.lower() in ['n', 'no']:
        break

# print a message when the game is over
print("Thanks for playing!")
