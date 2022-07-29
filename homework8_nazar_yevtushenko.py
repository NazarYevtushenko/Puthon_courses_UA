
# Task1. 5 points
# Написать функцию которая будет принимать 3 аргумента (int) и находить максимум из них '''

def max_from3(num1, num2, num3):
    return max(num1, num2, num3)

print(max_from3(2,8,5))

# Task2. 10 points
# Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
# Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать 3 аргумента и находить максимум с помощью функции1.
# в итоге будет .

def max_from3(num1, num2, num3):
    def max_from2(num1, num2):
        return max(num1, num2)
    return max(num3, max_from2(num1, num2))

print(max_from3(13, 7, 10))#

# Task 3. 10 points Lambda function. с помощью Анонимной функции остортировать
# список кортежей по цифре.

list_tuple = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
x = sorted(list_tuple, key=lambda nums: nums[1])

print(x)


# Task 4. 30 points познакомиться с модулем datetime и написать программу с помощью lambda
# для возвращение текущего года, месяца , дня
# например результат должен быть таким

import datetime
now = datetime.datetime.now()
year = lambda now: now.year
month = lambda now: now.strftime("%B")
day = lambda now: now.day

print(year(now))
print(month(now))
print(day(now))
# # скинуть мне ссылку на документацию по datetime.

# https://docs.python.org/3/library/datetime.html - Это официальная
# https://www.w3schools.com/python/python_datetime.asp - Я работал по этой