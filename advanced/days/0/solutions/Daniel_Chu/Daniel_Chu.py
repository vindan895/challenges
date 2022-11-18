import math
file_name = "Day_0"
author = "Daniel Chu"
email = "chud002@tcdsb.ca"

#Code Starts

#Code to find hypotenuse
hypo = math.sqrt(2546375247**2 + 45987482082**2)

#Finds the area
side_a = (2546375247)
side_b = (45987482082)
area = (int(side_a) + int(side_b))/2
print(area)
#Finds the perimeter
perimeter = (int(side_a) + int(side_b) + int(hypo))
print(perimeter)
