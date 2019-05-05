quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
#for letter in quote:
#    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#        print(letter, end="")


#for i in range(0,100,7):
#    print(i)

# Modify this loop to stop when i is exactly divisible by 11
#for i in range(0, 100, 7):
#    if i % 11 == 0:
#        print(i)
#        break

for i in range(1,21):
    print(i)
    if (i % 3 == 0) or (i % 5 == 0):
        continue