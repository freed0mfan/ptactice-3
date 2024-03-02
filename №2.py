time = int(input('Время в секундах: '))
hours = time // (60 * 60)
mins = (time % (60 * 60)) // 60
secs = (time % (60 * 60)) % 60
print(f'Текущее время: {hours} ч, {mins} мин, {secs} сек')
