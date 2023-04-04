from typing import Dict, List


def calculate_average_score(n: int, marks: Dict[str, List[float]], query_name: str) -> float:
    """
    Calculates the average score for the given student's name.

    Args:
        n (int): The number of students.
        marks (Dict[str, List[float]]): A dictionary containing the name and scores of each student.
        query_name (str): The name of the student whose average score is to be calculated.

    Returns:
        float: The average score of the given student.
    """
    if query_name not in marks:
        raise ValueError(f"{query_name} is not a valid student name.")

    scores = marks[query_name]
    return round(sum(scores) / len(scores), 2)


if __name__ == '__main__':
    # Prompt the user to input the number of students
    n = int(input("Enter the number of students: "))

    # Initialize an empty dictionary to store the name and scores of each student
    marks = {}

    # Prompt the user to input the name and scores of each student
    for i in range(n):
        name = input(f"Enter the name of student #{i + 1}: ")
        score_str = input(f"Enter the scores of {name} (comma-separated): ")

        # Convert the score string to a list of floats
        try:
            scores = [float(score.strip()) for score in score_str.split(",")]
        except ValueError:
            print(f"Invalid input: {score_str}. Scores must be comma-separated numbers.")
            continue

        # Add the name and scores to the marks dictionary
        marks[name] = scores

    # Prompt the user to input the name of the student to calculate the average score for
    query_name = input("Enter the name of the student to calculate the average score for: ")

    # Calculate and print the average score for the given student
    try:
        avg_score = calculate_average_score(n, marks, query_name)
        print(f"The average score for {query_name} is: {avg_score:.2f}")
    except ValueError as e:
        print(str(e))
