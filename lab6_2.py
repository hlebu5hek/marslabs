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
Четность номера фрукта в одном дне должна быть разная
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
        if len(order) > 0:
            if order[-1] % 2 == i % 2:
                continue
        npool = []
        npool.extend(pool)
        npool.remove(i)
        norder = []
        norder.extend(order)
        norder.append(i)
        _c += 1
        shufleOrder(npool, norder)


fruits = [i for i in range(1, 16)]
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
c = int(input("Количество выводимых вариантов : "))
_c = 0
shufleOrder(fruits)
ordersit = list(itertools.islice(itertools.permutations(fruits, 15), c**2))

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
            print('ф', order[j], end=' ', sep='')
            j += 1
    print()

print('\nРезультат работы itertools : ')
i = 0

for order in ordersit:
    if i >= c: break
    t = 0
    for j in range(0, 14, 2):
        if order[j] % 2 == order[j+1] % 2:
            t = 1
            break
    if t == 1:
        continue
    print('Случай {:} : '.format(i + 1))
    i += 1
    j = 0
    for day in range(7):
        print(' | ', days[day], end=' : ')
        for k in range(2):
            print('ф', order[j], end=' ', sep='')
            j += 1
    print()