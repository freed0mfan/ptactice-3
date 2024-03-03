x = int(input('x: '))
y = int(input('y: '))

result = int((x % y == 0) or (y % x == 0))
print(result)
