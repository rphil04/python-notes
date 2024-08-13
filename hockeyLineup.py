"""
Hockey Lineup Ice Time Calculator
=================================

This script calculates the expected time on ice and number of shifts per player 
based on the number of skaters available and the shift duration. The script 
divides skaters into forwards and defensemen, then calculates the time on ice 
and expected shifts for each position.

Functions:
----------
calculate_time(skaters, shift_duration)
    Calculates and prints the time on ice and expected shifts for forwards 
    and defensemen.

main()
    The main function that interacts with the user to gather input and 
    display the results.

Usage:
------
Run the script and provide the number of skaters and shift duration when prompted.
"""

def calculate_time(skaters, shift_duration):
    game_duration = 60  # Game duration in minutes

    # Determine the number of forwards and defensemen based on the number of skaters
    if skaters == 5:
        forwards, defense = 3, 2
    elif skaters in [6, 7]:
        forwards, defense = skaters - 2, 2
    elif skaters in [8, 9]:
        forwards, defense = skaters - 3, 3
    elif skaters == 10:
        forwards, defense = 6, 4
    elif skaters == 11:
        forwards, defense = 7, 4
    elif skaters == 12:
        forwards, defense = 7, 5
    elif skaters == 13:
        forwards, defense = 8, 5
    elif skaters in [14, 15]:
        forwards, defense = 9, skaters - 9
    else:
        forwards = skaters * 9 // 15
        defense = skaters - forwards

    # Calculate time on ice and expected shifts
    total_forward_time = game_duration * 60  # Convert game duration to seconds
    time_on_ice = total_forward_time / (forwards * shift_duration)
    total_defense_time = game_duration * 60  # Convert game duration to seconds
    defense_time_on_ice = total_defense_time / (defense * shift_duration)

    total_shifts = (game_duration * 60) // shift_duration
    shifts_per_forward = total_shifts // forwards
    shifts_per_defense = total_shifts // defense

    # Output results
    print("\033[0;32mStrategy\033[0m")
    print(f"  Number of Forwards: \033[0;32m{forwards}\033[0m")
    print(f"  Time on Ice per Forward: \033[0;32m{time_on_ice:.2f} minutes\033[0m")
    print(f"  Expected Shifts per Forward: \033[0;32m{shifts_per_forward} shifts\033[0m")
    print(f"  Number of Defense: \033[0;34m{defense}\033[0m")
    print(f"  Time on Ice per Defenseman: \033[0;34m{defense_time_on_ice:.2f} minutes\033[0m")
    print(f"  Expected Shifts per Defenseman: \033[0;34m{shifts_per_defense} shifts\033[0m")

def main():
    print("Hockey Lineup Ice Time Calculator")
    skaters = int(input("Enter the number of skaters available: "))
    if skaters < 5:
        print("You need at least 5 skaters to run a game.")
        return

    shift_duration = int(input("Enter the shift duration (in seconds): "))
    calculate_time(skaters, shift_duration)

if __name__ == "__main__":
    main()
