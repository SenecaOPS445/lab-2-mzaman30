#!/usr/bin/env python3
import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit()

name = sys.argv[1]  # First argument is name
age = sys.argv[2]   # Second argument is age

print(f'Hi {name}, you are {age} years old.')
