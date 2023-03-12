# Task21_3 к уроку №21 (10.03.23)

# Условие:
# Создайте таблицу book с полями book_id(int), book_title(text),
# book_author(text), publisher_id(int) (Введите несколько книг нескольких авторов.
# Сделайте несколько SELECT для выборки книг по авторам, по названиям.

# CREATE TABLE book
# (book_id int,
# book_title text,
# book_author text,
# publisher_id int)

# SELECT * FROM book

# INSERT INTO book VALUES
# (1, 'Три товарища', 'Э. М. Ремарк', 1),
# (2, 'Последний из могикан', 'Ф. Купер', 2),
# (3, 'Пнин', 'В. Набоков', 3),
# (4, 'Бегущая по волнам', 'А. С. Грин', 1)

# SELECT book_id, book_title, book_author, publisher_id FROM book WHERE publisher_id = 1
# SELECT book_id, book_title, book_author, publisher_id FROM book WHERE book_id = 2
# SELECT book_id, book_title, book_author, publisher_id FROM book WHERE book_title = 'Три товарища'