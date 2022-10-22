# Summary
# In the number guessing game, you guess a number between 1 and 10, while a random number generator
# generates random numbers within the same range. You get 3 chances to get it right or the game is over.

# Note: Error checks are in place for integers only. 
# Room for improvement: Add error checks for floats and strings.

# Import the random module
import random
from curses.ascii import isdigit

# Define global variables here
count = 1

# Add functions for reusable code
def errorCheck():
    global x
    if x.isdigit() and int(x) in range(1,10):
        print("great")
    else:
        print("Make sure the value you entered is an integer in the range between 1 and 10") 

def errorCheck2():
    y = str(uNumber)
    if y.isdigit() and int(y) in range(1,10):
        print("great")
    else:
        print("Make sure the value you entered is an integer in the range between 1 and 10") 

def successful():
    print('Congratulations, you guessed correctly!')
    print('The game is now over. See you again next time!')

def fail():
    # declare the variables are from the global scope
    global uNumber,gNumber,count
    while uNumber != gNumber:
        if count == 3:
            print('You lose. You have exceeded the number of valid attempts. Try again later.')
            exit()
        else:
            count = count + 1
            print('Your guess was incorrect, try again')
            uNumber = int(input())
            errorCheck2()
            #print('You guessed', uNumber, "location 2") # used for testing
            print('You guessed', uNumber)
            if uNumber == gNumber:
                successful()
                continue

# Computer generates a number
gNumber = random.randint(1,10)
print(gNumber)

# Prompt user to guess the number. Add error check
print('Guess a number between 1 and 10')
x = input()
errorCheck()
uNumber = int(x)
print('You guessed', uNumber)

# Check if user guessed correctly
if uNumber == gNumber:
    successful()

# Otherwise, incorrect guess gets 2 more attempts
else:
    fail()