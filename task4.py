#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math
print("You are trying to solve the surface area of your cone")
We = "height="
Did = "Radius="
The = int(input(We))
Mash = int(input(Did))
MonsterMash = math.pi*Mash*(Mash+math.sqrt(The**2+Mash**2))
print(f"the surface area is {MonsterMash}")