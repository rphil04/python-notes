#!/usr/bin/env python3

# Hockey Lineup Ice Time Calculator
# =================================
#
# This script calculates the expected time on ice and number of shifts per player
# based on the number of skaters available and the shift duration. The script
# provides two strategies:
#
# Strategy 1: Set Positions
#     Divides skaters into forwards and defense, then calculates the time
#     on ice and expected shifts for each position.
#
# Strategy 2: No Set Positions
#     Assumes all skaters rotate through shifts equally, regardless of position.
#
# Functions:
# ----------
# calculate_time(skaters, shift_duration)
#     Calculates and prints the time on ice and expected shifts for forwards,
#     defense, and for a scenario without set positions.
#
# Usage:
# ------
# Run the script and provide the number of skaters and shift duration when prompted.

def calculate_time(skaters, shift_duration):
    game_duration = 60  # Default game duration in minutes

    # Calculate the number of forwards and defense based on skaters
    if skaters == 5:
        forwards, defense = 3, 2
    elif skaters == 6:
        forwards, defense = 4, 2
    elif skaters == 7:
        forwards, defense = 4, 3
    elif skaters in (8, 9):
        forwards, defense = skaters - 3, 3
    elif skaters == 10:
        forwards, defense = 6, 4
    elif skaters == 11:
        forwards, defense = 7, 4
    elif skaters == 12:
        forwards, defense = 7, 5
    elif skaters == 13:
        forwards, defense = 8, 5
    elif skaters in (14, 15):
        forwards, defense = 9, skaters - 9
    else:
        forwards = skaters * 9 // 15
        defense = skaters - forwards

    # Strategy 1: Set Positions
    total_forward_time = game_duration * 60  # Convert game duration to seconds
    time_on_ice = total_forward_time / (forwards * shift_duration)
    total_defense_time = game_duration * 60  # Convert game duration to seconds
    defense_time_on_ice = total_defense_time / (defense * shift_duration)

    total_shifts = total_forward_time / shift_duration
    shifts_per_forward = total_shifts / forwards
    shifts_per_defense = total_shifts / defense

    print("\033[0;32mStrategy 1: Set Positions\033[0m")
    print(f"  Number of Forwards: \033[0;32m{forwards}\033[0m")
    print(f"  Time on ice per Forward: \033[0;32m{time_on_ice:.2f} minutes\033[0m")
    print(f"  Expected shifts per Forward: \033[0;32m{shifts_per_forward:.2f} shifts\033[0m")
    print(f"  Number of Defense: \033[0;34m{defense}\033[0m")
    print(f"  Time on ice per Defense: \033[0;34m{defense_time_on_ice:.2f} minutes\033[0m")
    print(f"  Expected shifts per Defense: \033[0;34m{shifts_per_defense:.2f} shifts\033[0m")

    # Strategy 2: No Set Positions
    time_on_ice_2 = total_forward_time / (skaters * shift_duration)
    shifts_per_player = total_shifts / skaters

    print("\n\033[0;34mStrategy 2: No Set Positions\033[0m")
    print(f"  Time on ice per Player: \033[0;32m{time_on_ice_2:.2f} minutes\033[0m")
    print(f"  Expected shifts per Player: \033[0;34m{shifts_per_player:.2f} shifts\033[0m")


def main():
    print("Hockey Lineup Ice Time Calculator")
    try:
        skaters = int(input("Enter the number of skaters available: "))
        if skaters < 5:
            print("You need at least 5 skaters to run a game.")
            return

        shift_duration = int(input("Enter the shift duration (in seconds): "))
        calculate_time(skaters, shift_duration)

    except ValueError:
        print("Please enter valid integers for skaters and shift duration.")


if __name__ == "__main__":
    main()
