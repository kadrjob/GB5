
DAY = 86400
HOUR = 3600
MINUTE = 60

duration = int(input('Введите продолжительность '))

if duration > DAY:
    d = duration // DAY
    h = (duration - d * DAY) // HOUR
    m = (duration - (d * DAY + h * HOUR)) // MINUTE
    s = duration - (d * DAY + h * HOUR + m * MINUTE)
    my_str = f'{d} дн {h} час {m} мин {s} сек'
elif DAY > duration > HOUR:
    h = duration // HOUR
    m = (duration - h * HOUR) // MINUTE
    s = duration - (h * HOUR + m * MINUTE)
    my_str = f'{h} час {m} мин {s} сек'
elif HOUR > duration > MINUTE:
    m = duration // MINUTE
    s = duration - (m * MINUTE)
    my_str = f'{m} мин {s} сек'
else:
    my_str = f'{duration} сек'

print(f'duration {duration}')
print(my_str)
