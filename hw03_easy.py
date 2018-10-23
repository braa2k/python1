__author__ = 'Sergey Bakhonin'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    result = number
    decad = 10 ** ndigits
    n = result * decad
    if n - int(n) >= 0.5:
         result = (int(n) + 1) / decad
    else:
        result = int(n) / decad
    return result

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    s = str(ticket_number)
    return len(s) == 6 and (int(s[0]) + int(s[1]) + int(s[2]) == int(s[3]) + int(s[4]) + int(s[5]))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))