#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math
question = "what is the radius of the sphere?"
Ghost = int(input(question))
Scary = 4/3*math.pi*Ghost**3
print(f"The radius of your sphere is {Ghost} and your volume is {Scary}")