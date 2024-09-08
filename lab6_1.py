'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 3. У няни 15 разных фруктов (ф1,…ф7).
Сформировать (вывести) все возможные варианты меню полдника (2 фрукта)
для ребенка на неделю.
'''
import itertools
import math

orders = []
_c = 0
def shufleOrder(pool, order=[]):
    global _c
    if len(pool) < 1:
        orders.append(order)
        return
    if _c > c**2:
        return
    for i in pool:
        npool = []
        npool.extend(pool)
        npool.remove(i)
        norder = []
        norder.extend(order)
        norder.append(i)
        _c += 1
        shufleOrder(npool, norder)


fruits = ["ф" + str(i + 1) for i in range(15)]
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
c = int(input("Количество выводимых вариантов : "))
_c = 0
shufleOrder(fruits)
ordersit = list(itertools.islice(itertools.permutations(fruits, 15), c))
countsit = list(itertools.islice(itertools.product([2], repeat=7), c))

print('Результат работы алгоритма : ')
i = 0
for order in orders:
    if i >= c: break
    print('Случай {:} : '.format(i + 1))
    i += 1
    j = 0
    for day in range(7):
        print(' | ', days[day], end=' : ')
        for k in range(2):
            print(order[j], end=' ')
            j += 1
    print()

print('\nРезультат работы itertools : ')
i = 0
for order in ordersit:
    if i >= c: break
    for count in countsit:
        if i >= c: break
        if sum(count) > 15: continue
        print('Случай {:} : '.format(i + 1))
        i += 1
        j = 0
        for day, count in enumerate(count):
            print(' | ', days[day], end=' : ')
            for k in range(count):
                print(order[j], end=' ')
                j += 1
        print()
