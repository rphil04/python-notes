#!/usr/bin/env python3

"""
Hockey Lineup Generator and Lineup Ice Time Calculator
------------------------------------------------------
This script generates a hockey lineup based on the availability of players 
and calculates the expected time on ice for forwards and defensemen. 
It considers unavailable players, fills underfilled positions with suggested 
players, and ensures the lineup and strategy outputs are accurate and consistent.

Main Features:
1. Handles unavailable players.
2. Suggests players to fill underfilled positions based on predefined preferences.
3. Removes players from their original position if moved to another.
4. Accurately calculates and displays the number of forwards and defensemen 
   along with their respective time on ice.
5. Color-coded output for better readability.

Usage:
1. Run the script.
2. Input unavailable players when prompted.
3. If a position is underfilled, select a player from the suggested list.
4. Review the generated lineup and strategy output.

Author: [Your Name]
Last Updated: [Date]
"""

#!/usr/bin/env python3

import random


def calculate_time(forwards_count, defense_count):
    game_duration = 60  # Game duration in minutes
    total_game_time = game_duration * 60  # Convert game duration to seconds

    # Calculate time on ice per forward and defenseman in seconds
    time_on_ice_forward = total_game_time / (forwards_count / 3)
    time_on_ice_defense = total_game_time / (defense_count / 2)

    print("\033[0;35mStrategy: Set Positions\033[0m")
    print(f"  Number of Forwards: \033[0;32m{forwards_count}\033[0m")
    print(f"  Time on ice per Forward: \033[0;32m{time_on_ice_forward / 60:.2f} minutes\033[0m")
    print(f"  Number of Defense: \033[0;34m{defense_count}\033[0m")
    print(f"  Time on ice per Defense: \033[0;34m{time_on_ice_defense / 60:.2f} minutes\033[0m")


def generate_lineup(unavailable_players):
    centers = ["Michael Belaen", "Thomas Hillebrand", "Gretchen Kjorstad"]
    right_wings = ["Bridget Gallagan", "Tyler VanEps", "Jim Francis", "Josh Rosenberg"]
    left_wings = ["Tom Kopischke", "Jesse Kimes", "Ryan Smith", "Nate Lee"]
    right_defense = ["Trey Crooks", "Edward Joseph"]
    left_defense = ["Robbie Phillips", "Joe Kluver"]

    centers = [player for player in centers if player not in unavailable_players]
    right_wings = [player for player in right_wings if player not in unavailable_players]
    left_wings = [player for player in left_wings if player not in unavailable_players]
    right_defense = [player for player in right_defense if player not in unavailable_players]
    left_defense = [player for player in left_defense if player not in unavailable_players]

    used_players = set(centers + right_wings + left_wings + right_defense + left_defense)

    # Count available skaters
    available_skaters = len(centers + right_wings + left_wings + right_defense + left_defense)

    # Adjust required positions based on the number of skaters
    if available_skaters < 13:
        required_positions = {
            "Centers": 2,
            "Right Wings": 2,
            "Left Wings": 2,
            "Right Defense": 2,
            "Left Defense": 2
        }
    else:
        required_positions = {
            "Centers": 3,
            "Right Wings": 3,
            "Left Wings": 3,
            "Right Defense": 2,
            "Left Defense": 2
        }

    positions = {
        "Centers": centers,
        "Right Wings": right_wings,
        "Left Wings": left_wings,
        "Right Defense": right_defense,
        "Left Defense": left_defense
    }

    def remove_player_from_positions(player):
        for pos in positions:
            if player in positions[pos]:
                positions[pos].remove(player)

    def get_suggested_players(position_name):
        suggestions = {
            "Centers": ["Josh Rosenberg", "Ryan Smith", "Bridget Gallagan"],
            "Right Wings": ["Ryan Smith", "Michael Belaen", "Jesse Kimes", "Thomas Hillebrand", "Trey Crooks",
                            "Edward Joseph"],
            "Left Wings": ["Tyler VanEps", "Jim Francis", "Josh Rosenberg", "Joe Kluver", "Edward Joseph"],
            "Right Defense": ["Tyler VanEps", "Thomas Hillebrand", "Nate Lee", "Josh Rosenberg"],
            "Left Defense": ["Tyler VanEps", "Thomas Hillebrand", "Nate Lee", "Josh Rosenberg"]
        }
        return [player for player in suggestions.get(position_name, []) if player not in unavailable_players]

    def fill_underfilled_positions():
        for pos, needed_count in required_positions.items():
            while len(positions[pos]) < needed_count:
                available_suggested_players = get_suggested_players(pos)
                if not available_suggested_players:
                    print(f"\033[0;31mNo available players to fill {pos}.\033[0m")
                    break
                print(f"\033[0;31m{pos} is underfilled.\033[0m")
                print(f"\033[0;33mSuggested players: {available_suggested_players}\033[0m")
                player_to_add = input(f"Please enter the name of a player to fill {pos}: ").strip()
                if player_to_add in available_suggested_players:
                    remove_player_from_positions(player_to_add)
                    positions[pos].append(player_to_add)
                    used_players.add(player_to_add)
                else:
                    print(f"{player_to_add} is not a valid choice or is already in use.")

    fill_underfilled_positions()

    available_skaters = positions["Centers"] + positions["Right Wings"] + positions["Left Wings"] + \
                        positions["Right Defense"] + positions["Left Defense"]
    skaters_count = len(available_skaters)

    # Count forwards and defense
    num_forwards = len(positions["Centers"]) + len(positions["Right Wings"]) + len(positions["Left Wings"])
    num_defense = len(positions["Right Defense"]) + len(positions["Left Defense"])

    print("\033[0;36mLineup Based on Availability\033[0m")
    print(f"  Available Skaters: {skaters_count}")
    print(f"  Centers: {positions['Centers']}")
    print(f"  Right Wings: {positions['Right Wings']}")
    print(f"  Left Wings: {positions['Left Wings']}")
    print(f"  Right Defense: {positions['Right Defense']}")
    print(f"  Left Defense: {positions['Left Defense']}")

    starting_lineup = {
        "Center": random.choice(positions["Centers"]),
        "Right Wing": random.choice(positions["Right Wings"]),
        "Left Wing": random.choice(positions["Left Wings"]),
        "Right Defense": random.choice(positions["Right Defense"]),
        "Left Defense": random.choice(positions["Left Defense"])
    }

    print("\033[1;33mStarting Lineup\033[0m")
    for position, player in starting_lineup.items():
        print(f"  {position}: {player}")

    calculate_time(num_forwards, num_defense)

    return skaters_count


def main():
    print("Hockey Lineup Generator and Lineup Ice Time Calculator")

    unavailable_players = input("Enter the names of unavailable players separated by commas: ").split(',')
    unavailable_players = [player.strip() for player in unavailable_players]

    skaters = generate_lineup(unavailable_players)

    if skaters < 5:
        print("You need at least 5 skaters to run a game.")
        return


if __name__ == "__main__":
    main()
