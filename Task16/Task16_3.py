# Task16_3 к уроку №16 (22.02.23)

# Условие:
# Создайте декоратор, который переводит все слова к следующему виду,
# первая буква в верхнем регистре, а остальные в нижнем.

def speak(text):
    def whisper(t):
        return t.title()
    return whisper(text)
print(speak(input()))
