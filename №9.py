import math

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

a_b = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
a_c = math.degrees(math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * a * c)))
b_c = 180 - a_b - a_c
print(a_b, a_c, b_c)
