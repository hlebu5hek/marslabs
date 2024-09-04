'''
Вариант 3.
Натуральные числа.
Выводит на экран числа, которые не содержат цифры, введенной с клавиатуры.
Первое и последнее число выводятся прописью.
'''
import re
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'} #Словарь с цифрами
file_name = "text.txt" #Выбор файла
k = '128'
k0 = False #Встретилось ли число, состоящее из нулей
with open(file_name, 'r') as file:
    f = file.readlines()
    for i, gived_num in enumerate(f):
        gived_num = gived_num.replace('\n', '')
        if re.match("^[0-9]+$", gived_num) and not re.search("[{0}]".format(k), gived_num):
            print(dc_cifr[gived_num[0]], end=' ')
            print(gived_num[1: len(gived_num) - 1], end=' ')
            print(dc_cifr[gived_num[-1]])