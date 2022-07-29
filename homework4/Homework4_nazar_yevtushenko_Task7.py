#---+---+---+---+---+#
# Homework #4. Task 7#
#  Nazar Yevtushenko #
#---+---+---+---+---+#


in_list: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
out_list: list = []

for a in in_list:
    out_list.append(list(a))

print(out_list)