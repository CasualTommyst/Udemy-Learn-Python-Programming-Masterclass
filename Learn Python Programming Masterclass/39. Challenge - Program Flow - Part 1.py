# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.
import sys
address = str(input("Please add the address here: "))
segmentCount = 1
segmentLength = []
counter = ""
validchars = ["0","1","2","3","4","5","6","7","8","9","."]

for i in address:
    if i not in validchars:
        print("This doesn't look like a valid IP address.")
        sys.exit(0)

if len(address) == 0:
    print("The address contains 0 segments.")
else:
    if "." not in address:
        print("This doesn't look like an IP address.")
        segmentCount = 0
    else:
        for i in address:
            if i != ".":
                counter += i
            elif i == ".":
                segmentLength.append(len(counter))
                counter = ""
                segmentCount += 1
        segmentLength.append((len(counter)))
        print("The address contains {} segments.".format(segmentCount))
        for count, item in enumerate(segmentLength, start=1):
            print("Segment {0} is {1} characters long.".format(count, item))