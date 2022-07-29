#---+---+---+---+---+#
# Homework #4. Task 9#
#  Nazar Yevtushenko #
#---+---+---+---+---+#

list1: list = [1,3]
list2: list = [2,4,1]
equal: bool = None

for x in list1:
    for y in list2:
        if x == y:
            print("В списках есть схожие элементы")
            equal = True
            break