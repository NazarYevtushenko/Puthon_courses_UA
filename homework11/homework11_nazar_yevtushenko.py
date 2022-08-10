from iterator import *

# TODO 2
# Скинуть файлик с примерами всех конструкций КРОМЕ менеджера контекста.
# With/as. 20 баллов

# try:
#     # a/0
#     3/0
# except ZeroDivisionError:
#     print('Division by Zero')
# except (ValueError, TypeError) as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     pass
# finally:
#     pass
#
# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# try:
#     raise MyError('Попытка № 5')
# except MyError as me:
#     print(me)
#
# numberberber = 42
# assert numberberber > 0 and isinstance(number, int), \
#     f"number greater than 0 expected, got: {numberberber}"

# TODO 3
# Задача 20 баллов написать функцию которая принимает от пользователя 2 аргумента
# и делит оlин на другой.
# при попытке деления на ноль вывести пользователю
# "ай яй яй делить на ноль можно не многим"
# Все остальные исключения с поймать и вывести их значение в текстовом формате.
# И в любом случае вывести. " I 'am happy that you learn python"

def div(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        print("ай яй яй делить на ноль можно не многим")
    except Exception as ex:
        print(ex)
    finally:
        print("I'am happy that you learn python")


# TODO 5
# 20 баллов Попробовать понять. Патерн Итератор
# https://refactoring.guru/ru/design-patterns/iterator/python/example

# collections = WordsCollection()
# collections.add_item("1")
# collections.add_item("2")
# collections.add_item("3")
#
# print("Прямой обход")
# print("\n".join(collections))
#
# print("Обратный обход")
# print("\n".join(collections.reverse_iterator()))

# TODO 6
# Попробовать посмотреть на написанный код и сделать его более надежным. Любые изменения приветствуются.
# просмотреть каждую программу и посмотреть как она может упасть. Попробовать ее зафейлить.

# def example1():
#     for i in range(3):
#         try:
#             x = int(input("enter a number: "))
#             y = int(input("enter another number: "))
#             print(x, '/', y, '=', x / y)
#         except ZeroDivisionError:
#             print('Пожалуйста, не делите на ноль')
#         except ValueError:
#             print('Пожалуйста, вводите только целые числа')

#Возможные ошибки:
#Zero Division y = 0
#ValueError x or y = str
#ValueError x or y = float


# def example2(L):
#     print("\n\nExample 2")
#     sum = 0
#     sumOfPairs = []
#     try:
#         sumOfPairs = [L[i] + L[i+1] for i in range(len(L)) if i != len(L)-1]
#     except TypeError:
#         print("Пожалуйста, введите список целых чисел")
#     except Exception as err:
#         print(err)
#     else:
#         print(f"{sumOfPairs = }")

# IndexError: list index out of range. Изначально ошибка содержалась в sumOfPairs.append(L[i] + L[i + 1])
# TypeError L = object of type 'int' has no len() input: 10
# TypeError L = unsupported operand type(s) for +: 'int' and 'str' input: [23, str]
# KeyError: если передаешь словарь input: {23: 10, 22: 1}
# IndexError: tuple index out of range input: (23,32,13,10)


# def printUpperFile( fileName ):
#     try:
#         with open( fileName, "r" ) as file:
#             for line in file:
#                 print(line.upper())
#     except FileNotFoundError:
#         print('Пожалуйста, введите правильное расположение файлов')

#Основной фейл - это отсутствие файла. Изменил close на with для того, чтобы точно файл закрылся
#Ошибки типов не имеют значения, так как из строки считывается тип str

def main():
    # Task 3 Test
    # div(1, '3')

    #Task 6
    # L = [ 10, 3, 5, 6, 9, 3 ]
    # example2(L)
    # example2([ 10, 3, 5, 6, "NA", 3 ])
    # example3( [ 10, 3, 5, 6 ] )
    # printUpperFile("doesNotExistYest.txt")
    # printUpperFile("./Dessssktop/misspelled.txt")

if __name__ == '__main__':
    main()
