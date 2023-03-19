# Task24_3 к уроку №24 (17.03.23)

# Условие:
# Создайте функцию, которая принимает на входе строку из круглых скобок,
# открывающих и закрывающих, и возвращает True или False , если строка
# является «правильной», т.е. никогда количество закрывающих не больше,
# чем количество открывающих, если двигаться по строке слева направо.

def check(string):
    brackets_open = ('(')
    brackets_closed = (')')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                return False
    return (not stack)

str1 = '()'
str2 = ')(()))'
str3 = '('
str4 = '(()) (( ()() ) () )'

print(check(str1))  #True
print(check(str2))  #False
print(check(str3))  #True
print(check(str4))  #False