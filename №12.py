N = float(input('N: '))

hours = N // (360 / 12)
minutes = (N % (360 / 12)) // (360 / (12 * 60))

print(f'{int(hours)} ч. и {int(minutes)} мин.')
