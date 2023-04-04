if __name__ == '__main__':
    try:
        # Prompt user to enter the number of integers in the list
        n = int(input("Enter the number of integers in the list: "))

        # Prompt user to enter the integers separated by spaces and convert them to a list
        arr = list(map(int, input("Enter the integers separated by spaces: ").split()))

        # Check that the list has at least 2 integers, otherwise raise an error
        if len(arr) < 2:
            raise ValueError("List must have at least 2 integers.")
    except ValueError as e:
        # Print error message if user input is invalid
        print("Error: ", e)
    else:
        # Sort the list in ascending order
        arr.sort()

        # Print the second largest element in the list
        print("The second largest element in the list is:", arr[-2])
