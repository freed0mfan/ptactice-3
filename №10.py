parameters = ['ATT', 'COMP', 'YDS', 'TD', 'INT']
values = []
for i in range(len(parameters)):
    values.append(int(input(f'{parameters[i]}: ')))

ATT = values[0]
COMP = values[1]
YDS = values[2]
TD = values[3]
INT = values[4]

a = ((COMP / ATT) - 0.3) * 5
b = ((YDS / ATT) - 3) * 0.25
c = (TD / ATT) * 20
d = 2.375 - (INT / ATT) * 25

passer_rating = ((a + b + c + d) / 6) * 100

print(passer_rating)
