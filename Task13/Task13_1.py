# Task13_1  к уроку №13 (15.02.23)

# Условие:
# Создайте функцию-генератор, которая создает бесконечную последовательность:
# 1, 2, 3, 4, 5, 6, …


import time
# Создаем функцию генератор
def fu():
# Создаем переменную n
    n = 0
# Создаем бесконечный цикл
    while True:
        n += 1
# Используя yield создаем условие if для четных и нечетных чисел
        yield n if n % 2 == 1 else n * -1
# оздаем новую переменную и создаем цикл
gf = fu()
for i in gf:
# Выводим на печать в строчку и используем таймер для последовательного вывода чисел
    print(i, end = ', ')
    time.sleep(1)
