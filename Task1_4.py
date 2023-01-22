#Task 1_4 к уроку №1 (18.01.23)

# Условие:
# Введите два числа x и y.
# Напечатайте наибольшее из числе x+y, x-y, x*y, x/y, x//y.

# Вводим первое число
x = int(input("Введите число x: "))

# Вводим второе число
y = int(input("Введите число y: "))

# Проверяем второе число на равенство нулю
if y == 0:
    print("Ошибка, на ноль делить нельзя!")
    exit()

# Присваиеваем новые переменные
else:
    a = (x + y)
    b = (x - y)
    c = (x * y)
    d = (x / y)
    e = (x // y)

# Выводим значения x и y, которые мы ввели
    print("x =", x, "; " "y =", y)

# Сравниваем между собой переменные
if a > b and a >= c and a > d and a > e:
    print(a)
elif b > a and b > c and b > d and b > e:
    print(b)
elif c > a and c > b and c > d and c > e:
    print(c)
elif d > a and d > b and d > c and d > e:
    print(d)
else:
    print(e)