english_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
english_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
russian_lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
russian_upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print("Введите сдвиг: ")
key = int(input())
print("Введите текст: ")
text = input()
def my_function(k, t):
    for i in range(len(t)):
        if t[i] in russian_upper_alphabet:
            print(russian_upper_alphabet[(russian_upper_alphabet.index(t[i]) + k) % len(russian_upper_alphabet)], end='')
        elif t[i] in english_upper_alphabet:
            print(english_upper_alphabet[(english_upper_alphabet.index(t[i]) + k) % len(russian_upper_alphabet)], end='')
        elif t[i] in russian_lower_alphabet:
            print(russian_lower_alphabet[(russian_lower_alphabet.index(t[i]) + k) % len(russian_lower_alphabet)], end='')
        elif t[i] in english_lower_alphabet:
            print(english_lower_alphabet[(english_lower_alphabet.index(t[i]) + k) % len(english_lower_alphabet)], end='')
        else:
            print(t[i], end='')
my_function(key, text)