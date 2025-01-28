#!/usr/bin/env python3

# Author: Your Full Name
# Author ID: Your Seneca ID
# Date Created: 2025/01/22

import sys  # Import sys module to handle command-line arguments

# Assign the value from the first command-line argument to 'timer' (convert it to integer)
timer = int(sys.argv[1])

# While loop that counts down from the timer value to 1
while timer > 0:
    print(timer)  # Print the current value of timer
    timer -= 1  # Decrement timer by 1 after each loop

# When the loop ends, print 'blast off!'
print('blast off!')
