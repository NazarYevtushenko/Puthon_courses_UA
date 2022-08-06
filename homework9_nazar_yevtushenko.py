#TASK 1. Написати функцію котра буде рахувати сумму зі списку чисел.
# ваша_функція([1, 2, 3, 4, 5, 6, 7, 8])

def sum_built(list):
    return sum(list)

def sum_own(list):
    sum = 0
    for i in list:
        sum += i
    return sum

# TASK 2. Написати функцію котра буде повертати сумму зі вложених списків також. Приклад
# ваша_.функція([1, 2, [3, 4, [5, 6], 7], 8])

def sum_recursion(in_list):
    sum = 0
    for i in in_list:
        if not type(i) is list:
            sum += i
        else:
            sum += sum_recursion(i)
    return sum

    if type(i) is list:
        sum += sum_recursion(i)
    else:
        return

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [1, 2, [3, 4, [5, 6], 7], 8]

    print(sum_built(list1))
    print(sum_built(list1))
    print(sum_recursion(list2))