import math

SIDE_1 = 2546375247 
SIDE_2 = 45987482082

area = (SIDE_1 * SIDE_2) / 2

hyp = math.sqrt((SIDE_1 ** 2) + (SIDE_2 ** 2))

perimeter = SIDE_1 + SIDE_2 + hyp

print(area)
print(perimeter)
