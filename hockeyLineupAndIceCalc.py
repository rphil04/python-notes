# ============================================================
# Hockey Lineup Generator and Ice Time Calculator
# ============================================================
# Description:
#   This script generates a hockey lineup based on player 
#   availability and calculates the ice time for forwards 
#   and defensemen based on the game duration.
#
#   The script checks for invalid player names (due to 
#   spelling errors) against a list of known players and 
#   prompts the user to re-enter names if necessary, ensuring 
#   that the lineup is generated correctly with known players only.
#
#   If any positions are underfilled due to unavailable players, 
#   the script suggests available players to fill those positions, 
#   allowing the user to assign them as needed.
#
# Key Functions:
#   - calculate_time(forwards_count, defense_count):
#       Calculates and displays the ice time per forward 
#       and defenseman based on the total game duration.
#
#   - validate_player_names(player_names):
#       Validates the provided player names against a list 
#       of known players to detect any spelling errors.
#
#   - generate_lineup(unavailable_players):
#       Generates the hockey lineup based on available 
#       players, fills any underfilled positions, and selects 
#       a starting lineup randomly from available players.
#
#   - get_unavailable_players():
#       Handles the input of unavailable players and their validation.
#
#   - main():
#       Orchestrates the input, validation, lineup generation, 
#       and ice time calculation process.
#
# Usage:
#   Run the script and enter the names of unavailable 
#   players when prompted. The script will guide you through 
#   any corrections if needed and display the final lineup.
# ============================================================

#!/usr/bin/env python3

import random
from enum import Enum

# Position Enum
class Position(Enum):
    CENTER = "Centers"
    RIGHT_WING = "Right Wings"
    LEFT_WING = "Left Wings"
    RIGHT_DEFENSE = "Right Defense"
    LEFT_DEFENSE = "Left Defense"

# Constants
GAME_DURATION_MINUTES = 60
KNOWN_PLAYERS = [
    "Michael Belaen", "Thomas Hillebrand", "Gretchen Kjorstad", "Bridget Gallagan",
    "Tyler VanEps", "Jim Francis", "Josh Rosenberg", "Tom Kopischke",
    "Jesse Kimes", "Ryan Smith", "Nate Lee", "Trey Crooks",
    "Edward Joseph", "Robbie Phillips", "Joe Kluver"
]

# Calculates time on ice per player based on number of forwards and defense
def calculate_time(forwards_count, defense_count):
    total_game_time = GAME_DURATION_MINUTES * 60
    time_on_ice_forward = total_game_time / (forwards_count / 3)
    time_on_ice_defense = total_game_time / (defense_count / 2)

    print("\033[0;35mStrategy: Set Positions\033[0m")
    print(f"  Number of Forwards: \033[0;32m{forwards_count}\033[0m")
    print(f"  Time on ice per Forward: \033[0;32m{time_on_ice_forward / 60:.2f} minutes\033[0m")
    print(f"  Number of Defense: \033[0;34m{defense_count}\033[0m")
    print(f"  Time on ice per Defense: \033[0;34m{time_on_ice_defense / 60:.2f} minutes\033[0m")

# Validates player names against known players
def validate_player_names(player_names):
    invalid_names = [name for name in player_names if name not in KNOWN_PLAYERS]
    if invalid_names:
        print("\033[0;31mInvalid player names detected:\033[0m", invalid_names)
        print("Please check spelling and restart the script.")
        return False
    return True

# Handles the input of unavailable players and validation
def get_unavailable_players():
    while True:
        unavailable_players = input("Enter the names of unavailable players separated by commas: ").split(',')
        unavailable_players = [player.strip() for player in unavailable_players]
        if validate_player_names(unavailable_players):
            return unavailable_players

# Generates the hockey lineup based on availability and user input
def generate_lineup(unavailable_players):
    positions = {
        Position.CENTER: ["Michael Belaen", "Thomas Hillebrand", "Gretchen Kjorstad"],
        Position.RIGHT_WING: ["Bridget Gallagan", "Tyler VanEps", "Jim Francis", "Josh Rosenberg"],
        Position.LEFT_WING: ["Tom Kopischke", "Jesse Kimes", "Ryan Smith", "Nate Lee"],
        Position.RIGHT_DEFENSE: ["Trey Crooks", "Edward Joseph"],
        Position.LEFT_DEFENSE: ["Robbie Phillips", "Joe Kluver"]
    }

    # Remove unavailable players
    for position_key in positions:
        positions[position_key] = [player for player in positions[position_key] if player not in unavailable_players]

    # Count available skaters and adjust position requirements
    available_skaters = sum(len(players) for players in positions.values())
    required_positions = {position_key: 2 for position_key in positions} if available_skaters < 13 else {Position.CENTER: 3, Position.RIGHT_WING: 3, Position.LEFT_WING: 3, Position.RIGHT_DEFENSE: 2, Position.LEFT_DEFENSE: 2}

    def remove_player_from_positions(player):
        for position_key in positions:
            if player in positions[position_key]:
                positions[position_key].remove(player)

    def get_suggested_players(position_key):
        suggestions = {
            Position.CENTER: ["Josh Rosenberg", "Ryan Smith", "Bridget Gallagan"],
            Position.RIGHT_WING: ["Ryan Smith", "Michael Belaen", "Jesse Kimes", "Thomas Hillebrand", "Trey Crooks", "Edward Joseph"],
            Position.LEFT_WING: ["Tyler VanEps", "Jim Francis", "Josh Rosenberg", "Joe Kluver", "Edward Joseph"],
            Position.RIGHT_DEFENSE: ["Tyler VanEps", "Thomas Hillebrand", "Nate Lee", "Josh Rosenberg"],
            Position.LEFT_DEFENSE: ["Tyler VanEps", "Thomas Hillebrand", "Nate Lee", "Josh Rosenberg"]
        }
        return [player for player in suggestions.get(position_key, []) if player not in unavailable_players]

    # Fill underfilled positions
    for position_key, needed_count in required_positions.items():
        while len(positions[position_key]) < needed_count:
            available_suggested_players = get_suggested_players(position_key)
            if not available_suggested_players:
                print(f"\033[0;31mNo available players to fill {position_key.value}.\033[0m")
                break
            print(f"\033[0;31m{position_key.value} is underfilled.\033[0m")
            print(f"\033[0;33mSuggested players: {available_suggested_players}\033[0m")
            player_to_add = input(f"Please enter the name of a player to fill {position_key.value}: ").strip()
            if player_to_add in available_suggested_players:
                remove_player_from_positions(player_to_add)
                positions[position_key].append(player_to_add)
            else:
                print(f"{player_to_add} is not a valid choice or is already in use.")

    num_forwards = sum(len(positions[position_key]) for position_key in [Position.CENTER, Position.RIGHT_WING, Position.LEFT_WING])
    num_defense = sum(len(positions[position_key]) for position_key in [Position.RIGHT_DEFENSE, Position.LEFT_DEFENSE])

    # Display lineup
    print("\033[0;36mLineup Based on Availability\033[0m")
    for position_key, players in positions.items():
        print(f"  {position_key.value}: {players}")

    starting_lineup = {position_key.name.replace("_", " ").title(): random.choice(players) for position_key, players in positions.items()}

    print("\033[1;33mStarting Lineup\033[0m")
    for position_name, player in starting_lineup.items():
        print(f"  {position_name}: {player}")

    calculate_time(num_forwards, num_defense)

# Main function
def main():
    print("Hockey Lineup Generator and Ice Time Calculator")
    unavailable_players = get_unavailable_players()
    generate_lineup(unavailable_players)

if __name__ == "__main__":
    main()
