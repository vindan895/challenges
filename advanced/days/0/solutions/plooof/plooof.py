import math

measurement1 = 2546375247
measurement2 = 45987482082

m1sq = measurement1 * measurement1
m2sq = measurement2 * measurement2
m3sq = m1sq + m2sq

measurement3 = math.sqrt(m3sq)

area = (measurement1 * measurement2) / 2
perimeter = measurement1 + measurement2 + measurement3

print(area)
print(perimeter)