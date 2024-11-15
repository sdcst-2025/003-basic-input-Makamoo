#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

import math
print("You are looking for x in the equation ax + b = c:")
Spooky = "a="
Scary = "b="
Skeletons = "c="
Send = int(input(Spooky))
Shivers = int(input(Scary))
Down = int(input(Skeletons))
YourSpine = (Down-Shivers)/Send
print(f"x={YourSpine}")