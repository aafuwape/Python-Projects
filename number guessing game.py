# Summary
# In the number guessing game, you guess a number between 1 and 5, while a random number generator
# generates random numbers within the same range. You get 3 chances to get it right or the game is over.

# Import the random module
import random

count = 1
# Computer generates a number
gNumber = random.randint(1,10)
print(gNumber)

# Prompt user to guess the number. Add error check
print('Guess a number between 1 and 10')
uNumber = int(input())
print('You guessed', uNumber)

# Check if user guessed correctly
if uNumber == gNumber:
    print('Congratulations, you guessed correctly!')
    print('The game is now over. Try again next time!')

# Otherwise, incorrect guess
# Check if your guess is correct. If correct, you win, otherwise, try again 2 more times and then the game ends.
else:
    while uNumber != gNumber:
        if count == 3:
            print('You lose. You have exceeded the number of valid attempts. Try again later.')
            break
        else:
            count = count + 1
            print('Your guess was incorrect, try again')
            uNumber = int(input())
            if uNumber == gNumber:
                print('Congratulations, you guessed correctly!')
                print('The game is now over. Try again next time!')
            continue