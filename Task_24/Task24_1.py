# Task24_1 к уроку №24 (17.03.23)

# Условие:
# Напишите функцию, которая сортирует числовой список,
# не используя никаких функций, вроде sort sorted и т.д.



def s(num):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return num
lst = [150, 234, 2, 34, 54, 1, 22, 3, 4, 5, 90, 23]
print(s(lst))