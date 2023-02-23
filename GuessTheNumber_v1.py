import random

print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
print("Number Guessing Game")
print("You get five chances to guess the number")
print("If you do not guess in time, you lose!")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")

# User can choose the range of numbers to guess from
range_start = int(input("Enter the starting number for the range: "))
range_end = int(input("Enter the ending number for the range: "))
number = random.randint(range_start, range_end)

chances = 0
score = 0
high_score = float('inf')

print("Guess a number between", range_start, "and", range_end)

# User only has 5 chances
while(chances < 5):
    guess = int(input())
    if guess == number:
        print("~*~*~*~*~*~*~*~*~*")
        print("You Won!")
        print("~*~*~*~*~*~*~*~*~*")
        score = 5 - chances
        print("Your score is", score)
        if score < high_score:
            high_score = score
            print("Congratulations! You set a new high score!")
        break
    elif guess < number:
        print("Try a higher number!")
    else:
        print("Try a lower number!")

    # Indicate how close the user is to the correct answer
    if abs(guess - number) <= 2:
        print("You are very close!")
    elif abs(guess - number) <= 5:
        print("You are getting warmer!")

    chances += 1

if not chances < 5:
    print("Too bad! You ran out of guesses! The number was", number)
    print("Your score is", score)

print("The high score is", high_score)