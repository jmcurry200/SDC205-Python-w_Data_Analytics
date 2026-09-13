# Jenice Curry
# 09/12/26
# This program demonstrates proficiency with
# Decisions, Loops, Processing, Output and Formatting


name = input("What is your name? ")
studentID = input("What is your studentID? ")

number = 5
outputStr = ''
guessCount = 0

# Get the number from the user.
guess = int(input('Guess and enter a number between 1 and 10.'))

while guess != -1:
# Determine if user's choice is valid.  
    if guess <1 or guess > 10:
        outputStr = 'Error: Invalid input'
        guessCount += 1
# Evaluate guess
    elif guess > number:
        outputStr = 'Error: Your guess is too high.'
        guessCount += 1

    elif guess < number:
        outputStr = 'Error: Your guess is too low.'
        guessCount += 1
    else:
       outputStr = f'Congratulations, {name}!  You guessed the correct number in {guessCount} tries!'

    print(outputStr)
    guess = int(input('Enter number if you would like to guess again or enter -1 to quit): '))






