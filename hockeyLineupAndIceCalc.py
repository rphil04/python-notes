# ============================================================
# Hockey Lineup Generator and Ice Time Calculator
# ============================================================
# Description:
#   This script generates a hockey lineup based on player 
#   availability and calculates the ice time for forwards 
#   and defensemen based on the game duration.
#
#   The script also checks for invalid player names (due 
#   to spelling errors) and prompts the user to re-enter 
#   names if needed, ensuring that the lineup is generated 
#   correctly with known players only.
#
# Key Functions:
#   - calculate_time(forwards_count, defense_count):
#       Calculates and displays the ice time per forward 
#       and defenseman based on the total game duration.
#
#   - validate_player_names(player_names, known_players):
#       Validates the provided player names against a list 
#       of known players to detect any spelling errors.
#
#   - generate_lineup(unavailable_players):
#       Generates the hockey lineup based on available 
#       players, fills any underfilled positions, and selects 
#       a starting lineup randomly from available players.
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

# Function to calculate the time on ice for forwards and defensemen
def calculate_time(forwards_count, defense_count):
    game_duration = 60  # Game duration in minutes
    total_game_time = game_duration * 60  # Convert game duration to seconds

    # Calculate time on ice per forward and defenseman in seconds
    time_on_ice_forward = total_game_time / (forwards_count / 3)
    time_on_ice_defense = total_game_time / (defense_count / 2)

    # Display the strategy for setting positions, including the number of players and their time on ice
    print("\033[0;35mStrategy: Set Positions\033[0m")
    print(f"  Number of Forwards: \033[0;32m{forwards_count}\033[0m")
    print(f"  Time on ice per Forward: \033[0;32m{time_on_ice_forward / 60:.2f} minutes\033[0m")
    print(f"  Number of Defense: \033[0;34m{defense_count}\033[0m")
    print(f"  Time on ice per Defense: \033[0;34m{time_on_ice_defense / 60:.2f} minutes\033[0m")

# Function to validate player names against known players
def validate_player_names(player_names, known_players):
    invalid_names = [player for player in player_names if player not in known_players]
    if invalid_names:
        print(f"\033[0;31mError: The following names do not match any known player names: {', '.join(invalid_names)}. "
              f"Please check the spelling and try again.\033[0m")
        return False
    return True

# Function to generate the lineup based on the availability of players
def generate_lineup(unavailable_players):
    # Define the initial lists of players by position
    centers = ["Michael Belaen", "Thomas Hillebrand", "Gretchen Kjorstad"]
    right_wings = ["Bridget Gallagan", "Tyler VanEps", "Jim Francis", "Josh Rosenberg"]
    left_wings = ["Tom Kopischke", "Jesse Kimes", "Ryan Smith", "Nate Lee"]
    right_defense = ["Trey Crooks", "Edward Joseph"]
    left_defense = ["Robbie Phillips", "Joe Kluver"]

    # Combine all players into one list for validation purposes
    all_known_players = centers + right_wings + left_wings + right_defense + left_defense

    # Validate the unavailable players
    if not validate_player_names(unavailable_players, all_known_players):
        return 0  # Return to prompt user to enter names again

    # Remove unavailable players
    centers = [player for player in centers if player not in unavailable_players]
    right_wings = [player for player in right_wings if player not in unavailable_players]
    left_wings = [player for player in left_wings if player not in unavailable_players]
    right_defense = [player for player in right_defense if player not in unavailable_players]
    left_defense = [player for player in left_defense if player not in unavailable_players]

    # Track used players to avoid duplicates
    used_players = set(centers + right_wings + left_wings + right_defense + left_defense)

    # Count available skaters
    available_skaters = len(centers + right_wings + left_wings + right_defense + left_defense)

    # Adjust the required positions based on the number of available skaters
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

    # Store the positions and their corresponding players in a dictionary
    positions = {
        "Centers": centers,
        "Right Wings": right_wings,
        "Left Wings": left_wings,
        "Right Defense": right_defense,
        "Left Defense": left_defense
    }

    # Function to remove a player from all positions
    def remove_player_from_positions(player):
        for pos in positions:
            if player in positions[pos]:
                positions[pos].remove(player)

    # Function to get suggested players for a position
    def get_suggested_players(position_name):
        suggestions = {
            "Centers": ["Josh Rosenberg", "Ryan Smith", "Bridget Gallagan"],
            "Right Wings": ["Ryan Smith", "Michael Belaen", "Jesse Kimes", "Thomas Hillebrand", "Trey Crooks", "Edward Joseph"],
            "Left Wings": ["Tyler VanEps", "Jim Francis", "Josh Rosenberg", "Joe Kluver", "Edward Joseph"],
            "Right Defense": ["Tyler VanEps", "Thomas Hillebrand", "Nate Lee", "Josh Rosenberg"],
            "Left Defense": ["Tyler VanEps", "Thomas Hillebrand", "Nate Lee", "Josh Rosenberg"]
        }
        return [player for player in suggestions.get(position_name, []) if player not in unavailable_players]

    # Function to fill underfilled positions
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

    # Fill underfilled positions with user input
    fill_underfilled_positions()

    # Recalculate the number of available skaters after adjustments
    available_skaters = positions["Centers"] + positions["Right Wings"] + positions["Left Wings"] + \
                        positions["Right Defense"] + positions["Left Defense"]
    skaters_count = len(available_skaters)

    # Count the number of forwards and defensemen
    num_forwards = len(positions["Centers"]) + len(positions["Right Wings"]) + len(positions["Left Wings"])
    num_defense = len(positions["Right Defense"]) + len(positions["Left Defense"])

    # Display the final lineup based on availability
    print("\033[0;36mLineup Based on Availability\033[0m")
    print(f"  Available Skaters: {skaters_count}")
    print(f"  Centers: {positions['Centers']}")
    print(f"  Right Wings: {positions['Right Wings']}")
    print(f"  Left Wings: {positions['Left Wings']}")
    print(f"  Right Defense: {positions['Right Defense']}")
    print(f"  Left Defense: {positions['Left Defense']}")

    # Select the starting lineup randomly from the available players
    starting_lineup = {
        "Center": random.choice(positions["Centers"]),
        "Right Wing": random.choice(positions["Right Wings"]),
        "Left Wing": random.choice(positions["Left Wings"]),
        "Right Defense": random.choice(positions["Right Defense"]),
        "Left Defense": random.choice(positions["Left Defense"])
    }

    # Display the starting lineup
    print("\033[1;33mStarting Lineup\033[0m")
    for position, player in starting_lineup.items():
        print(f"  {position}: {player}")

    # Calculate and display the time on ice for forwards and defensemen
    calculate_time(num_forwards, num_defense)

    return skaters_count

# Main function to run the lineup generator
def main():
    print("Hockey Lineup Generator and Lineup Ice Time Calculator")

    # Prompt the user to input unavailable players
    while True:
        unavailable_players = input("Enter the names of unavailable players separated by commas: ").split(',')
        unavailable_players = [player.strip() for player in unavailable_players]

        skaters = generate_lineup(unavailable_players)

        # If the lineup generation is successful, break the loop
        if skaters > 0:
            break

    # Ensure there are enough skaters to play the game
    if skaters < 5:
        print("You need at least 5 skaters to run a game.")
        return

# Entry point of the script
if __name__ == "__main__":
    main()
