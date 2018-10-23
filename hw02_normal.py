__author__ = 'Sergey Bakhonin'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
list = [2, -5, 8, 9, -25, 25, 4]
newlist = [math.sqrt(m) for m in list if m>=0 and math.sqrt(m)%1==0]
print(newlist)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = '02.11.2013'
dd,mm,yyyy = date.split('.')
days = {'1':'первое','2':'второе','3':'третье','4':'четвертое','5':'пятое','6':'шестое','7':'седьмое','8':'восьмое','9':'девятое','10':'десятое',
        '11':'одиннадцатое','12':'двеннадцатое','13':'тринадцатое','14':'четырнадцатое','15':'пятнадцатое','16':'шестнадцатое','17':'семнадцатое','18':'восемнадцатое','19':'девятнадцатое','20':'двадцатое',
        '21':'двадцать первое','22':'двадцать второе','23':'двадцать третье','24':'двадцать четвёртое','25':'двадцать пятое','26':'двадцать шестое','27':'двадцать седьмое','28':'двадцать восьмое','29':'двадцать девятое',
        '30':'тридцатое','31':'тридцать первое'}
months = {'1':'января','2':'февраля','3':'марта','4':'апреля','5':'мая','6':'июня','7':'июля','8':'августа','9':'сентября','10':'октября','11':'ноября','12':'декабря'}
dd = [s for k,s in days.items() if k==str(int(dd))]
mm = [s for k,s in months.items() if k==str(int(mm))]
print('{} {} {} года.'.format(dd[0], mm[0], yyyy))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
 
import random
list = []
n=int(input('Введите количество элементов списка: '))
for i in range(n):
    list.append(random.randint(-100,100))
print(list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
print('Исходный список:', lst)
lst2 = list(set(lst))
print('Уникальные элементы списка:', lst2)
lst3 = [i for i in lst if lst.count(i)==1]
print('Неповторяющиеся элементы списка:', lst3)
