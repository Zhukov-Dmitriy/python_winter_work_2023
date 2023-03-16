# Task23_3 к уроку №23 (15.03.23)

# Условие:
# Создайте функцию, на вход которой подается список из целых положительных чисел,
# и которая в качестве результата возвращает самое большое число, которое можно составить из этих чисел.
# Например, вход [1, 21, 3], результат 3211
# Если вход [9, 81, 25], то результат 98125.


def max_num(n):
    n = [str(i) for i in n]
    n = sorted(n, reverse = True)
    return ''.join(n)

num = [1, 21, 3]
print(max_num(num))
