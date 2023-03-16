# Task11_1 к уроку №11 (10.02.23)

# Условие:
#Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# Напечатайте список дат в 2023 году, когда вход бесплатен.


import calendar
year = 2023
lst = []

# Создаем два цикла (для месяца, и для дня)
# и с помощью методов calendar.monthrange и calendar.monthrange возвращаем даты
for month in range(1, 13):
    count = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        c = calendar.weekday(year, month, day)
        if c == 3:
            count += 1
            if count == 3:
                lst.append((month, day))
print("Список дат для бесплатного посещения Эрмитажа в 2023г.:", lst)