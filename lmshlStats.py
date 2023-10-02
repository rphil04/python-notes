"""
.SYNOPSIS
    Script to read and display player statistics from an Excel file for
    a specified team and filter the top players based on goals, assists, or points.

.DESCRIPTION
    This script allows users to interactively select a team's statistics
    from an Excel file and view player data. If the user selects League, the
    user can choose between the top 10 or top 25 players for each category, or estimate stats for a full 20-game season.

.PARAMETER excel_file
    The file path to the Excel file containing player statistics.

.NOTES
    File Name      : lmshlStats.py
    Author         :
    Prerequisite   : Python 3.9.6 or above
                        beautifulsoup4 Library for python
                        pandas library for Python
                        openpyxl Library for python
                        xlrd Library for python
    Copyright 2023 - All rights reserved.

.EXAMPLE
    python lmshlStats.py

    Prompts the user to select a team and filter options to display player statistics interactively.

"""
# import pandas
import pandas as pd
import numpy as np

# Define the file path
excel_file = '/Users/robbie/Desktop/S2-Stats.xlsx'

# Prompt the user to enter the team name
team_name = input(
    "Enter the team name (Boston, Dallas, Edmonton, New Jersey, Toronto, Detroit, New York, Philly, League): ")

# Define the desired column names
column_names = [
    'Player', 'GP', 'G', 'A', 'PTS', 'PIM', 'Plus/Minus',
    'Points per game', 'Shorthanded Goals', 'Hits', 'Faceoff Wins',
    'Faceoffs', 'Blocked Shots', 'Faceoff Wins %', 'Goals % per shot',
    'Interceptions', 'Giveaways', 'Takeaways', 'Passes Attempted',
    'Passes Complete', 'Hat Tricks'
]

try:
    # Read the selected team's sheet from the Excel file
    df = pd.read_excel(excel_file, sheet_name=team_name, usecols=range(0, 21), names=column_names)

    # Filter rows where 'Player' column is not empty
    df = df.dropna(subset=['Player'], how='all')

    # Display the DataFrame with the desired formatting
    pd.set_option('display.colheader_justify', 'center')  # Center-align column headers
    pd.options.display.float_format = '{:.0f}'.format  # Format numerical columns without '%'

    if team_name != 'League':
        print(df.to_string(index=False))

    while True:
        if team_name != 'League':
            # If a specific team is selected, restrict options to "Top 5" and "Top 10"
            print("\nChoose an option (1: Top 5, 2: Top 10, 0: Exit): ")
        else:
            # If "League" is selected, offer "Top 10," "Top 25," and "Estimate" options
            print("\nChoose an option (1: Top 10, 2: Top 25, 3: Estimate, 0: Exit): ")

        choice = input()

        if choice == '1':
            num_players = 5 if team_name != 'League' else 10  # Limit to Top 5 for teams other than League
        elif choice == '2':
            num_players = 10
        elif choice == '3' and team_name == 'League':
            # Estimate stats for a full 20-game season if "Estimate" is chosen in League
            df['G'] = df['G'] * 20 / df['GP']
            df['A'] = df['A'] * 20 / df['GP']
            df['PTS'] = df['PTS'] * 20 / df['GP']
            df['Rank'] = df['PTS'].rank(ascending=False, method='min', na_option='bottom').fillna(0).astype(int)
            print("\nEstimated Statistics for a Full 20-Game Season (Sorted by Points - High to Low):")
            print(df[['Rank', 'Player', 'G', 'A', 'PTS']].sort_values(by='PTS', ascending=False).to_string(index=False))
            continue
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        stat_choice = input("\nChoose a stat category (1: Goals, 2: Assists, 3: Points): ")

        if stat_choice == '1':
            stat_column = 'G'
            stat_name = 'Goal Scorers'
        elif stat_choice == '2':
            stat_column = 'A'
            stat_name = 'Assists Leaders'
        elif stat_choice == '3':
            stat_column = 'PTS'
            stat_name = 'Points Leaders'
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        # Display the top players based on the chosen category and number
        print(f"\nTop {num_players} {stat_name}:")
        top_players = df.sort_values(by=stat_column, ascending=False).head(num_players)
        top_players['Rank'] = top_players[stat_column].rank(ascending=False, method='min', na_option='bottom').fillna(0).astype(int)
        print(top_players[['Rank', 'Player', stat_column]].to_string(index=False))

except Exception as e:
    print(f"An error occurred: {e}")
