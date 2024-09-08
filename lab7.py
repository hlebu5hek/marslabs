'''
Вариант 3. У няни 15 разных фруктов (ф1,…ф7).
Сформировать (вывести) все возможные варианты меню полдника (2 фрукта)
для ребенка на неделю.
Подготовьте различные варианты поедания мороженного ребенком на неделю.
На следующий день нельзя есть больше мороженного, чем в предыдущий
'''
import itertools
import math
from tkinter import *
from tkinter import ttk

fruits = [i for i in range(1, 16)]
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
c = 15
_c = 0
itstrs = []
funcstrs = []

orders = []
counts = []
ordersit = []
countsit = []

root = Tk()
root.geometry('1200x840')
root.resizable(False, False)

labelc = ttk.Label(text="Количество выводимых вариантов: ")
labelc.place(anchor=NW, x = 30, y = 20, height = 25)
entryc = ttk.Entry()
entryc.place(anchor=NW, x = 250, y = 20, height = 25, width = 80)

labelit = ttk.Label(text="Результат Itertools : ")
labelit.place(anchor=NW, x = 30, y = 60, height = 25, width = 240)

labelal = ttk.Label(text="Результат алгоритма : ")
labelal.place(anchor=NW, x = 30, y = 420, height = 25, width = 240)

def drawScroll():
    itlist = StringVar(value=itstrs)
    listboxd = Listbox(listvariable=itlist)
    listboxd.place(anchor=NW, x=30, y=90, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=90, x=1150, width=20, height=320)
    listboxd["yscrollcommand"] = scrollbar.set

    funclist = StringVar(value=funcstrs)
    listboxt = Listbox(listvariable=funclist)
    listboxt.place(anchor=NW, x=30, y=450, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxt.yview)
    scrollbar.place(anchor=NW, y=450, x=1150, width=20, height=320)
    listboxt["yscrollcommand"] = scrollbar.set


drawScroll()

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



def countAll():
    global orders
    global ordersit
    _c = 0
    shufleOrder(fruits, [])
    ordersit = list(itertools.islice(itertools.permutations(fruits, 15), c**2))


def mainAlg():
    global c
    try:
        c = int(entryc.get())
    except:
        return

    i = 0
    for order in orders:
        if i >= c: break
        funcstrs.append('Случай {:} : '.format(i + 1))
        i += 1
        j = 0
        for day in range(7):
            funcstrs[-1] += ' | ' + days[day] + ' : '
            for k in range(2):
                funcstrs[-1] += 'ф' + str(order[j]) + ' '
                j += 1

    i = 0
    for order in ordersit:
        if i >= c: break
        t = 0
        for j in range(0, 14, 2):
            if order[j] % 2 == order[j + 1] % 2:
                t = 1
                break
        if t == 1:
            continue
        itstrs.append('Случай {:} : '.format(i + 1))
        i += 1
        j = 0
        for day in range(7):
            itstrs[-1] += ' | ' + days[day] + ' : '
            for k in range(2):
                itstrs[-1] += 'ф' + str(order[j]) + ' '
                j += 1

    drawScroll()


countAll()

btn = ttk.Button(text="Рассчитать", command=mainAlg)
btn.place(anchor=NW, x = 380, y = 20, height = 25, width = 100)

root.mainloop()