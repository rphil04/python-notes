def is_leap(year):
    """Check if a year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 400 == 0:     # If the year is divisible by 400, it's a leap year.
        return True
    elif year % 100 == 0:   # If the year is divisible by 100, it's not a leap year.
        return False
    elif year % 4 == 0:     # If the year is divisible by 4, it's a leap year.
        return True
    else:                   # Otherwise, it's not a leap year.
        return False

while True:
    try:
        year = int(input("Enter a year: "))   # Prompt the user to enter a year.
        if year <= 0:
            raise ValueError("Year must be positive.")    # Raise an error if the year is not positive.
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")  # Print an error message if the user enters invalid input.

if is_leap(year):
    print(f"{year} is a leap year.")    # Print a message indicating that the year is a leap year.
else:
    print(f"{year} is not a leap year.")    # Print a message indicating that the year is not a leap year.
