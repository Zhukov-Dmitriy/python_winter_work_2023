# Task19_1  к уроку №19 (03.03.23)

# Условие:
# В кошельке лежат бумажные купюры 50, 100, 200, 500, 1000, 5000 рублей, каждой купюры по одной штуке.
# Какие суммы можно составить, если использовать по три купюры из них?


import itertools
for x in itertools.combinations([50, 100, 200, 500, 1000, 5000], 3):
    print(f'{x}: {sum(x)}')
