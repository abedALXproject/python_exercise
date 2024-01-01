#!/usr/bin/python3

import time
from colorama import Fore
import pyfiglet

def count_sec(second):
    while second > 0:
        print(f"Time remaining: {second} second")
        time.sleep(1)
        second -= 1
    print("We Make it to 2024:)!")

try:
    seconds = int(input("Enter the countdown time in seconds: "))
    count_sec(seconds)
    newyear = pyfiglet.figlet_format(' Welcome to 2024 @innocent:) ')
    print(Fore.LIGHTGREEN_EX+newyear)
except ValueError:
    print("Invalid input. Please enter a valid number of seconds.")
