# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 35
answer = random.randint(1, highest)
print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
guessnumber = 1

while guess != answer:
    if guess == 0:
        print("Thank you for playing!")
        break
    elif guess < answer:
        print("Please guess higher")
        guessnumber += 1
        guess = int(input())
    elif guess > answer:
        print("Please guess lower")
        guessnumber += 1
        guess = int(input())
else:
    print("You got it on attempt #{}".format(guessnumber))
