# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == "__main__":
    n = int(input(f"enter your number: ").strip())

    even_odd = n // 2 == 0

    if even_odd and range(1,5):
        print('Not Weird')
    elif even_odd and range(6,20):
        print('Weird')
    elif even_odd and even_odd > 20:
        print('Not Weird')
    else:
        print('Weird')


