from functools import reduce

# Задача 1 10 баллов:
# Написать 3 примера генераторных функций с различными последовательностями.
#
def name_reverse(name: str) -> str:
    yield name[::-1]

def sum_list(list_num: list) -> int:
    yield sum(list_num)

def dict_sum(dict1, dict2: dict) -> dict:
    yield {**dict1, **dict2}
    yield dict1
    yield dict2

#
# Задача 2 10 баллов:
# Написать свою реализацию функции reduce() с описанием ее работы в однострочных и многострочных комментариях.
#
def my_reduce(func, iterable, last_elements = None):
    iterator = iter(iterable)
    if last_elements == None:
        value = next(iterator)
    else:
        value = last_elements
    for it in iterator:
        value = func(value, it)
    return value

def sums(a,b):
    return a+b


# Задача 3 30 баллов:
# Написать функцию которая с помощью assert будет тестировать ваш самопистный reduce

def my_reduce_test(func, test, last_element = None):
    try:
        assert (
                reduce(func, test, last_element) == my_reduce(func, test, last_element)), \
            'Func my_reduce works incorrect'
    except Exception as e:
        print(e)
    return reduce(func, test) == my_reduce(func, test)

lists = [2,4,5,6,7,8,12]
print(my_reduce_test(sums, lists))

# Задача 4. 30 баллов: Создать класс с методом которого можно будет возвращать область видимости(local)
# созданного экземпляра класса.
# В конструкторе(init) вашего класса пускай будут те параметры которые вы захотите.

class Locals:
    def __init__(self, name):
        self.name = name

    def locals_define(self):
        return self.__dict__

# Задача 6. бонусная задача C GitHub
# сгенерировать ssh ключь
# сохранить его в ГитХабе
# создать папку mkdir folder_name
# перейти в папку cd folder_name
# git clone адрес вашего репозитория
# сделать домашку.
# git add .
# git commit -m 'my first commit'
# git push

def main():
    # Task 1
    name_back = name_reverse("Nazar")
    print(next(name_back))
    sums = sum_list([2,4,3,2])
    print(next(sums))
    dict1 = {
        2:3,
        4:6
    }
    dict2 = {
        5:1,
        4:7
    }
    dict_union = dict_sum(dict1,dict2)
    print(next(dict_union))

    #Task 5
    tert = Locals("Define")
    print(tert.locals_define())

if __name__ == "__main__":
    main()