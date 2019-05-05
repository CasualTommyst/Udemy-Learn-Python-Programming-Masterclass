# for i in range(1, 12):
#     print("No {:<2} squared is {:<3} and cubed is {:<4}".format(i, i ** 2, i ** 3))
#     print("Calculation complete.")
#     print("Try again.")
#
# name = input("Please input your name: ")
# age = int(input("How old are you, {}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years.".format(18 - age))
#
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you've guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you've guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time!")
#
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#     else:  # if guess is greater than 5
#         print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you've guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time!")
#age = int(input("How old are you? "))
#
#if (age >= 16) and (age <= 65):
#    print("Have a good day at work!")
#elif (10 <= age <= 16):
#    print("You should be at school now!")
#else:
#    print("Whatever")
#
#x = "False"
#if x:
#    print("x is true")
#
#x = input("Please enter something: ")
#if x:
#    print("You've entered: {0}".format(x))
#else:
#    print("You did not enter anything!")
#
#print(not False)
#print(not True)
#
#age = int(input("How old are you? "))
#if not(age < 18):
#    print("You're old enough to vote!")
#    print("Please put an x in the box")
#else:
#    print("Please come back in {0} years.".format(18 - age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Bob.".format(letter))
else:
    print("I don't need that letter.")