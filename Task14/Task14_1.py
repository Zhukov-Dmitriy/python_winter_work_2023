# Task14_1 к уроку №14 (17.02.23)

# Условие:
# Напишите рекурсивную функцию, которая вычисляет количество
# цифр введенного натурального числа

def nch_len(n):
    if n == 0:
        return 0
    return 1 + nch_len(n // 10)
print(nch_len(int(input())))


