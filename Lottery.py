# Lottery.py
# Import.
import random

# Start prompt.
print('\n**** Welcome to the Pick-3, Pick-4 lottery number generator! ****')

# Menu prompt.
def menu():
    print('\n\nSelect from the following menu:\n\n1. Generate 3-Digit Lottery number\
    \n2. Generate 4-Digit Lottery number\n3. Exit the Application\n')

# Holds loop status in memory.
loop = True

# Sentinel while loop
while loop:
    menu()
    userInput = int(input())
    
# If-else statements performs proper operation for the user.
    if userInput == 1:
        print('\nYou selected 1. The following 3-digit lottery number was generated:\
            \n')
        for i in range(3):
            print(random.randrange(1, 10), end = '')
        
    if userInput == 2:
        print('\nYou selected 2. The following 4-digit lottery number was generated:\
            \n')
        for i in range(4):
            print(random.randrange(1, 10), end = '')
        
    if userInput == 3:
        print('\nYou selected 3.\n\nThanks for trying the Lottery Application.\
            \n\n*********************************************************\n')
        loop = False # Ends loop and consequently, the program.