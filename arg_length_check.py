#!/usr/bin/env python3
import sys

print(len(sys.argv))

if len(sys.argv) != 10:
    print('You do not have 10 arguments')
    sys.exit()
