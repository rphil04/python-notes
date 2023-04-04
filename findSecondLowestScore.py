"""
This script expects the user to provide the names and scores of the students as command line arguments.
For example, if the script is called second_lowest_score.py, you could run it like this: 
python second_lowest_score.py Alice 70 Bob 80 Charlie 60 Dave 90

This would produce the following output:
Alice
Bob
Dave
"""

import sys

# Initialize two empty lists to store student names and scores
students = []
scores = []

# Iterate over the command line arguments, skipping the first argument which is the name of the script itself
for arg in sys.argv[1:]:
    # Split the argument into name and score
    name, score = arg.split()
    # Convert the score to a float and append the score to the 'scores' list
    score = float(score)
    scores.append(score)
    # Append the name and score as a sub-list to the 'students' list
    students.append([name, score])

# Count the number of occurrences of the lowest score in the 'scores' list
count = scores.count(min(scores))
# Remove the lowest scores from the 'scores' list
for i in range(count):
    scores.remove(min(scores))

# The second-lowest score is now the new minimum score in the 'scores' list
secondHigh = min(scores)

# Sort the 'students' list in ascending order of name
students.sort()
# Create a new list 'output' that contains all sub-lists in the 'students' list whose second element (i.e., score) is equal to 'secondHigh'
output = [x for x in students if x[1] == secondHigh]
# Iterate over the 'output' list and print the first element (i.e., name) of each sub-list
for i in output:
    print(i[0])
