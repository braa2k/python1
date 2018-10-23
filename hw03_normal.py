__author__ = 'Sergey Bakhonin'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    i = 2
    lst = [1, 1]
    while i < m:
        a = lst[i - 1] + lst[i - 2]
        lst.append(a)
        i = i + 1
    return lst[n-1: m]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    b = origin_list
    c = True
    while c:
        c = False
        i = 0
        while i < len(b) - 1:
            h = b[i]
            l = b[i + 1]
            if h > l:
                b[i] = l
                b[i + 1] = h
                c = True
            i = i + 1
    print(b)
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# пример функции дающей true/false кастомному фильтру
def func(x):
     if x > 0:
             return 1
     else:
             return 0
# мой кастомный фильтр
def my_filter(func, a):
    for i in a:
        if func(i) == False:
            a.remove(i)
    return a
print(my_filter(func, a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def define_parallelogram(a1, a2, a3, a4):
     if abs(int(a1[0]) - int(a2[0])) == abs(int(a3[0]) - int(a4[0])) and abs(int(a1[1]) - int(a2[1])) == abs(int(a3[1]) - int(a4[1])):
          print("Является параллелограммом!")
     else:
          print("Не является параллелограммом!")
