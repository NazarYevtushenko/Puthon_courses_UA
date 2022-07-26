# Task 1
# сложить словари в один.
# использовать for и dict methods.

first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}

merged_dict = {**first, **second, **third, **fourth, **fifth} # 1 способ
merged_dict2 = {}
for item in (first, second, third, fourth,fifth):
    merged_dict2.update(item)

# Task 2. 10 points
# 1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
# 2. просуммировать все значения(values), делается в одну строку.(look build in functions)

pow2 = {}
sum1 = 0
for x in range(11,21):
    pow2[x] = x ** 2
    sum1 += pow2[x]

sum2 = sum(list(pow2)) #2 variant

# Task3. 5 points
# отсортировать словарь по ключам
task3 = {
    1: 23,
    78: 34,
    2: 43,
    11: 22,
    34: 41
}
task3_l = list(task3)
task3_l.sort()
task3_sorted = {}
for item in task3_l:
    task3_sorted[item] = task3[item]


# Task 4. 15
# Удалить дубликаты из dictionary

task4_dict = {'id1':{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},
'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
},
'id3':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
}
}
task4_final = {}
list_items = list(task4_dict.items())

for keys, items in list_items:
    if items not in list(task4_final.values()):
        task4_final[keys] = items

# print(task4_final)

# Task 5
# Вернуть из dictionary все уникальные values.
task5 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}
task5_result1 = set()

for i in task5:
    for b in i.values():
        task5_result1.add(b)

# Task 6. 15
# Посчитать общее количество наименований в списке. И только в списках.

shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
count = 0
for a, b in shedule.items():
    if type(b) == list:
        count+= len(b)
