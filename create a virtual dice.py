#create a virtual dice

# import random module
import random

# assign result of random integer to variable number. value must be between 1 and 6
number = str(random.randint(1,6))

# print output based on value.
if int(number) == 1:
    print('You got 1')
elif int(number) == 2:
    print('You got 2')
elif int(number) == 3:
    print('You got 3')
elif int(number) == 4:
    print('You got 4')
elif int(number) == 5:
    print('You got 5')
else:
    print('You got 6')