#!/usr/bin/env python3

# Hockey Lineup Ice Time Calculator
# =================================
#
# This script calculates the expected time on ice per player based on the number of
# skaters available. The script only provides one strategy:
#
# Strategy: Set Positions
#     Divides skaters into forwards and defense, then calculates the time
#     on ice for each position.
#
# Functions:
# ----------
# calculate_time(skaters)
#     Calculates and prints the time on ice for forwards and defense.
#
# Usage:
# ------
# Run the script and provide the number of skaters when prompted.

def calculate_time(skaters):
    game_duration = 60  # Game duration in minutes
    total_game_time = game_duration * 60  # Convert game duration to seconds

    # Calculate the number of forwards and defense based on skaters
    forwards = skaters * 3 // 5
    defense = skaters - forwards

    # Strategy: Set Positions

    # Calculate time on ice per forward and defenseman in seconds
    time_on_ice_forward = total_game_time / (forwards / 3)
    time_on_ice_defense = total_game_time / (defense / 2)

    print("\033[0;32mStrategy: Set Positions\033[0m")
    print(f"  Number of Forwards: \033[0;32m{forwards}\033[0m")
    print(f"  Time on ice per Forward: \033[0;32m{time_on_ice_forward / 60:.2f} minutes\033[0m")  # Converted to minutes
    print(f"  Number of Defense: \033[0;34m{defense}\033[0m")
    print(f"  Time on ice per Defense: \033[0;34m{time_on_ice_defense / 60:.2f} minutes\033[0m")  # Converted to minutes


def main():
    print("Hockey Lineup Ice Time Calculator")
    try:
        skaters = int(input("Enter the number of skaters available: "))
        if skaters < 5:
            print("You need at least 5 skaters to run a game.")
            return

        calculate_time(skaters)

    except ValueError:
        print("Please enter a valid integer for the number of skaters.")


if __name__ == "__main__":
    main()
