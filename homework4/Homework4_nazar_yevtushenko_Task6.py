#---+---+---+---+---+#
# Homework #4. Task 6#
#  Nazar Yevtushenko #
#---+---+---+---+---+#

def deleting_tup_el(tup):
    tup = (tup[0], tup[-1])
    return tup


list_tuple: tuple = (1, 3, 5, 7)
print(deleting_tup_el(list_tuple))