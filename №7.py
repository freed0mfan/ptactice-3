import math

x0 = 3.5
y0 = 6.5
x1 = 7.5
y1 = 0.5
d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
distance_m = 100 * d
print(int(round(distance_m)))
