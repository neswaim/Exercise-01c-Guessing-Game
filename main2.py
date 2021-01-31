#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

number = random.randrange(1,11)
count = 0
guess = -1
print("Welcome. Let's play a game, shall we?")
while guess != number:
    count = count + 1
    guess = input("Go ahead and guess a number from 1 to 10: ")
    try:
        guess = int(guess)
        if guess != number:
            print("Ah, you almost got it.")
    except:
        print("You seem confused. I said a number.")
print("Wow, so impressive! And it only took you " + str(count) + " tries.")