#to use lambda functions to calculate the circumference (CIR) of a circle in Python
from math import pi

calculate_cir = lambda r: 2 * pi * r
r = 5
cir = calculate_cir(r)
print(cir) # Output: 31.41592653589793
