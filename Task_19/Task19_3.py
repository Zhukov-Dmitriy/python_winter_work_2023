# Task19_3 к уроку №19 (03.03.23)

# Условие:
# Определите класс Person.
# При создании объекта p = Person(‘ Иванов ’, Михаил ’, Федорович ’’) необходимо ввести полное имя.
# При печати объекта должно выводиться следующее
# print(p) #чивородеФлиахиМвонавИ


class Person:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return ''.join(reversed(f'{self.a}, {self.b}, {self.c}')).replace(',', '').replace(' ', '')
p = Person('Иванов', 'Михаил', 'Федорович')
print(p)