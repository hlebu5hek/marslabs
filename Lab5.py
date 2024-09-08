"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
 Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
  Определить границы применимости рекурсивного и итерационного подхода.
   Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
3. F(1) = G(1) = 1; F(n) = (-1)n*(F(n–1) – 2*G(n–1)), G(n) = (n–1)! - G(n–1), при n >=2"""

import time
import matplotlib.pyplot as plt
from functools import lru_cache

n = -1

timer=[]
timer_rec=[]

one = -1
fp = 1

lru_cache(maxsize=None)
def fact(f):
    global fp
    fp *= f
    return fp


def rec_fg(x):
    global one
    if x == 1: return [1,1]
    p = rec_fg(x-1)
    one *= -1
    f = fact(x-1)
    return [one * (p[0] - 2*p[1]), f - p[1]]


def it_f(x):
    global one
    f = [1, 1]
    g = [1, 1]
    for i in range(1,x+1):
        one *= -1
        fc = fact(i)
        f[1] = one*(f[0] - 2*g[0])
        g[1] = fc - g[0]
        f[0], f[1] = f[1], f[0]
        g[0], g[1] = g[1], g[0]

    return f[1]

while n < 1:
    print("Введите натуральное число от 1 ")
    n = int(input())

graf = list(range(2, n+1))

for i in graf:
    start = time.time()
    one = 1
    fp = 1
    result = it_f(i)
    end = time.time()
    timer.append(end-start)
    start_rec = time.time()
    one = 1
    fp = 1
    res = rec_fg(i)[0]
    end_rec = time.time()
    timer_rec.append(end_rec-start_rec)
    print(i,
          " | Результат рекурсии ->", res,
          " | результат итерации ->", result,
          " | время  рекурсии ->", end_rec-start_rec,
          " | время  итерации ->",end-start)

#plt.plot(graf, timer, label='Итерационная функция.')
#plt.plot(graf, timer_rec, label='Рекусионная функция.')
#plt.legend(loc=2)

#plt.xlabel('Значение n')
#plt.ylabel('Время выполнения (c)')
#plt.show()