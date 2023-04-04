"""
The if __name__ == '__main__': block is the entry point of the script. It checks whether the script is being run as the main program or being imported as a module.

The script starts by initializing two empty lists students and scores. It then prompts the user to input the number of students and their respective names and scores. The range() function is used to iterate over the number of students, and for each iteration, the script prompts the user to input the name and score of the student. The name and score are then appended to the students list as a sub-list, while the score is also appended to the scores list.

After getting the input, the script counts the number of occurrences of the lowest score in the scores list and removes them one by one using a for loop. This ensures that the second-lowest score is the new minimum score in the scores list.

The script then assigns the second-lowest score to the variable secondHigh and sorts the students list in ascending order of name.

The next step is to create a new list called output using a list comprehension that contains all sub-lists in the students list whose second element (i.e., score) is equal to secondHigh. Finally, the script iterates over the output list and prints the first element (i.e., name) of each sub-list.

In summary, this script finds the second-lowest score among a list of students and prints the names of the students who have that score.
"""

# The following block of code is the entry point of the script
if __name__ == '__main__':
    # Initialize two empty lists to store student names and scores
    students = []
    scores = []
    
    # Prompt the user to input the number of students, and iterate over the number of students
    for N in range(int(input())):
        # Prompt the user to input the name and score of each student
        name = input()
        score = float(input())
        # Append the score to the 'scores' list, and append the name and score as a sub-list to the 'students' list
        scores.append(score)
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
