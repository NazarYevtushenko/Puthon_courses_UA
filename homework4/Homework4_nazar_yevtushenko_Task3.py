#---+---+---+---+---+#
# Homework #4. Task 3#
#  Nazar Yevtushenko #
#---+---+---+---+---+#


grocery_list = input("Please, insert your grocery list, separated by ',': ").split(",")

longest_word = ""
longest_lenght = 0

for product in grocery_list:
    if len(product) > longest_lenght:
        longest_word = product
        longest_lenght = len(product)

print('The longest name of product is {} with lenght of {} char'.format(longest_word, longest_lenght))
