#for i in range(1,20):
#    print("i is now {}".format(i))
#
#number = "9,213,543,743,101,255"
#for i in range(0, len(number)):
#    print(number[i])

number = "9,213,543,743,101,255"
cleaned_number = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleaned_number = cleaned_number + number[i]

newNumber = int(cleaned_number)
print("The number is {}".format(newNumber))