#Task5_1 к уроку №5 (27.01.23)

# Условие:
# Ввести число n.
# Напечатать треугольник Паскаля.

# Вводим число n
n = int(input("Введите число: "))
triangle = []
# С помощью циклов решаем. (решение подсмотрел в интернете)
for i in range(n):
    triangle.append([1] + [0] * n)
for i in range(1, n):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1] [j] + triangle [i - 1] [j - 1]
for i in range(0, n):
    for j in range(0, i + 1):
        print(triangle[i][j], end='')
    print()