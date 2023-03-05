# Task19_2 к уроку №19 (03.03.23)

# Условие:
# Реализуйте класс Fibonacci, который реализует итератор, генерирующий
# бесконечную последовательность чисел Фибоначчи.


class Fibonacci:
    def __init__(self):
        self.a = 1
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        fibonacci = self.a
        self.a, self.b = self.b, self.a + self.b
        return fibonacci
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
