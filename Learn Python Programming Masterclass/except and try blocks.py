# try:  # the try block tests for errors and instead of terminating, it raises an except-ion
#     Value = int(input("Type a number between 1 and 10: "))
# except (ValueError, KeyboardInterrupt):  # this except block determines which exceptions should act like this.
#     print("You must type a number between 1 and 10!")
# except:  # This is just here to handle any non-expected exceptions, but is something that should generally be avoided.
#     print("I did not expect this to happen!")
# else:
#     if (Value > 0) and (Value < 10):
#         print("You typed: ", Value)
#     else:
#         print("The value you typed is incorrect!")
#
#  #____________________________________________________________
#
# try:  # the try block tests for errors and instead of terminating, it raises an except-ion
#     Value = int(input("Type a number between 1 and 10: "))
# except ValueError:  # this except block determines which exceptions should act like this.
#     print("You must type a number. With numbers.")
# except KeyboardInterrupt:  # this except block determines which exceptions should act like this.
#     print("Oh dear, I'm afraid you've pressed something on your keyboard.")
# except:  # This is just here to handle any non-expected exceptions, but is something that should generally be avoided.
#     print("I did not expect this to happen!")
# else:
#     if (Value > 0) and (Value < 10):
#         print("You typed: ", Value)
#     else:
#         print("The value you typed is incorrect!")
#
#  #____________________________________________________________
# try:  # the try block tests for errors and instead of terminating, it raises an except-ion
#     Value = int(input("Type a number between 1 and 10: "))
# except KeyboardInterrupt:  # this except block determines which exceptions should act like this.
#     print("Oh dear, I'm afraid you've pressed something wrong on your keyboard.")
# except:  # This is just here to handle any non-expected exceptions, but is something that should generally be avoided.
#     print("I did not expect this to happen!")
# else:
#     if (Value > 0) and (Value < 10):
#         print("You typed: ", Value)
#     else:
#         print("The value you typed is incorrect!")
#
#  #____________________________________________________________
# TryAgain = True  # Here we define the initial truth value of our variable(?)/container(?)
# while TryAgain:  # The while loop ensures that a wrong answer doesn't terminate our code on the first problem.
#
#     try:
#         Value = int(input("Type a whole number. "))
#     except ValueError:
#         print("You must type a whole number!")
#
#         try:
#             DoOver = input("Try again (y/n)? ")
#         except:
#             print("OK, see you next time!")
#             TryAgain = False
#         else:
#             if str.upper(DoOver) == "N":  # The code in the book is unusable: any input except n/N equals "Y"
#                 TryAgain = False
#     except KeyboardInterrupt:
#         print("Oh dear, I'm afraid you've pressed something wrong on your keyboard.")
#         print("Sayonara!")
#         TryAgain = False
#     else:
#         print(Value)
#         TryAgain = False
#  #____________________________________________________________
# TryAgain = True  # Here we define the initial truth value of our variable(?)/container(?)
# while TryAgain:  # The while loop ensures that a wrong answer doesn't terminate our code on the first problem.
#
#     try:
#         Value = int(input("Type a whole number. "))
#     except ValueError:
#         print("You must type a whole number!")
#
#         try:
#             DoOver = input("Try again (y/n)? ")
#         except:
#             print("OK, see you next time!")
#             TryAgain = False
#         else:
#             if str.upper(DoOver) == "N":
#                 TryAgain = False
#             elif str.upper(DoOver) == "Y":  # the added elif statement helps ensuring the logic of the loop is kept.
#                 TryAgain = True
#             else:
#                 print("I've had enough of your shenanigans. Bye!")
#                 TryAgain = False
#     except KeyboardInterrupt:
#         print("Oh dear, I'm afraid you've pressed something wrong on your keyboard.")
#         print("Sayonara!")
#         TryAgain = False
#     else:
#         print(Value)
#         TryAgain = False
#  #____________________________________________________________
# try:
#     raise ValueError
# except ValueError:
#     print("What the Value!")
#  #____________________________________________________________
# ## why is the try needed here? let's see for ourselves!
# raise ValueError
# except ValueError:
#     print("What?!")
# ## well the why is still unknown but at least I know that the except needs its try.
#
# print('Hello There (Single Quote)!')
# print("Hello There (Double Quote)!")
# print("""This is a multiple line
# string using triple quotes.
# You can also use triple single quotes.""")
# print("""But what if I wish to use quotes like I'm some kind of "Dummy"?""")
# print('''"But what if
# I wish to use quotes
# like I'm some kind of "Dummy"?"''')
#  #____________________________________________________________
#
# print('\a \b \f \n \r \t  \v')
#
# print("Part of this text\r\nis on the next line.")
# print("This is an A with a grave accent: \xC0.")
# print("This is a drawing character: \u2562.")
# print("This is a pilcrow: \266.")
# print("This is a division sign: \xF7.")
#  #____________________________________________________________
