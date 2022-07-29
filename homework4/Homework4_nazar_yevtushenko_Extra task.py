#---+---+---+---+---+#
# Extra task. Matrix.#
# Nazar Yevtushenko. #
#---+---+---+---+---+#

#Обьявление переменных
s = '''  +---+---+---+---+---+
4 |   |   |   |   |   |
  +---+---+---+---+---+
3 |   |   |   |   |   |
  +---+---+---+---+---+
2 |   |   |   |   |   |
  +---+---+---+---+---+
1 |   |   |   |   |   |
  +---+---+---+---+---+
0 |   |   |   |   |   |
  +---+---+---+---+---+
    0   1   2   3   4'''
last_line = '''  +---+---+---+---+---+
    0   1   2   3   4'''
sep_line = '''  +---+---+---+---+---+ '''
sep_column = ' | '
print(s)
#Инициализация матрицы
matrix = []
for _ in range(5):
    matrix.append([' ',' ',' ',' ',' '])
# print(matrix)
choose = None
# Функция для проверки правильности ввода координат
def coordinate_check(str):
    while not str.isdigit():
        str = input('Некоректный ввод. Пожалуйста, введите в области от 0 до 4: ')
    while not int(str) in range(5):
        str = input('Некоректный ввод. Пожалуйста, введите в области от 0 до 4: ')
    else:
        return int(str)
# Функция для проверки правильности ввода menu
def menu_check(str):
    while not str.isdigit():
        str = input('Некоректный ввод. Пожалуйста, введите в области от 0 до 4: ')
    while not int(str) in range(5):
        str = input('Некоректный ввод. Пожалуйста, введите в области от 0 до 4: ')
    else:
        return int(str)

while not choose == 0:
    choose = menu_check(input('\nВыбери действие:\n1) Сделать запись \n2) Получить значение по координатам\n3) Показать все ячейки \n4) Удалить значение по координатам \n0) Программа завершает работу.\n'))

    # Ввод записи
    if choose == 1:
        x: int = coordinate_check(input('Введите x в формате от 0 до 4х: '))
        y: int = coordinate_check(input('Введите y в формате от 0 до 4х: '))
        value: str = input('Введите значение для записи: ')
        if matrix[x][y] == ' ':
            matrix[x][y] = value
            print(matrix)
            print('Запись сделана')
        else: #Если ячейка не пустая
            overwrite = int(input('Ячейка занята! Перезаписать?\n1) Да.\n2) НЕТ!\n'))
            if overwrite == 1:
                matrix[x][y] = value
                print('Запись сделана')
                
            else:
                continue #Переход к следующему оператору. В данном случае это ввод в меню
    # Вывод значения по координатам
    elif choose == 2:
        x: int = coordinate_check(input('Введите x в формате от 0 до 4х: '))
        y: int = coordinate_check(input('Введите y в формате от 0 до 4х: '))
        if matrix[x][y] == ' ':
            print('Ячейка пустая')
        else:
            print(f"Ваше значение: {matrix[x][y]}")
    # Показать все ячейки
    elif choose == 3:
        p_count = 4
        while p_count >= 0:
            print(sep_line)
            print(f'{p_count}{sep_column}' + sep_column.join(matrix[p_count])+f'{sep_column}')
            if p_count == 0: #Вывод последней строки
                print(last_line)
            p_count -= 1
    # Удалить значение по координатам
    elif choose == 4:
        x: int = coordinate_check(input('Введите x в формате от 0 до 4х: '))
        y: int = coordinate_check(input('Введите y в формате от 0 до 4х: '))
        matrix[x][y] = ' '
        print('Запись удалена')

# Exit program
print('Приходите еще =)')
input()