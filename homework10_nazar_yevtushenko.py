# TODO 1. 10 баллов

# Написать функцию которая будет добовлять код страны
# к номеру телефона с помощью замыкания
# внешний вид вызова функции.

def user_telephone(code: str) -> any:
    return lambda tel: code + tel


# TODO 2. 20 баллов

# Написать функцию которая будет у пользователя брать python обект в любом виде и выводить
# все его не магические методы в списке.
# и написать декторатор который будет выводить колличество методов в объекте.
# Похожую задачу мы уже решали. Можете взять решение из предыдущей . Но декоратор уже ваш полностью)

# Декоратор
def methods_amount(fun) -> any:
    def wrapper(type_in):
        return len(fun(type_in))

    return wrapper

# Основная функция
@methods_amount
def non_magic_metods(type_in) -> list:
    return [method for method in dir(type_in) if method[:2] != '__']


# TODO 3. 30 баллов

# дописать декоратор, чтобы он принимал аргумент, например текст.
# и выводил его тоже.

def text_out(text):
    def methods_amount_upg(fun):
        def wrapper(type_in):
            func = fun(type_in)
            print(text, len(func))

        return wrapper

    return methods_amount_upg


@text_out(text='Num')
def non_magic_metods3(type_in) -> list:
    return [method for method in dir(type_in) if method[:2] != '__']


# TODO 4. 30 баллов

# Ваша задача - создать декоратор для функции, которая принимает неограниченное количество позиционных
# ХЕШИРУЕМЫХ элементов.
# Декоратор добавляет следующий функционал:
# Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть результат выполнения этой функции
# из памяти, а не вычислять его заного.
# Если не вызывалась - вычислить результат, положить его в память, и вернуть.
# Подсказка - тут вам пригодятся словари.

SQUARE_HASH = {}

def square_sum_hash(fun):
    def wrapper(*args):
        if args in SQUARE_HASH.keys():
            result = SQUARE_HASH[args]
        else:
            result = fun(*args)
            SQUARE_HASH[args] = result
        return result

    return wrapper

@square_sum_hash
def square_sum(*args):
    return sum(arg ** 2 for arg in args)


def main():
    # TODO 1 Test

    my_number = user_telephone('+38044')
    print(my_number('838372893'))

    # TODO 2 Test
    print(non_magic_metods(type_in=tuple()))

    # TODO 3 Test

    non_magic_metods3(str())

    # TODO 4 Test
    print(square_sum(2, 2, 5, 6, 7, 6))
    print(square_sum(2, 1, 5, 3, 7, 6))
    print(SQUARE_HASH)


if __name__ == '__main__':
    main()
