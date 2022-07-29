#---+---+---+---+---+#
# Homework #4. Task 5#
#  Nazar Yevtushenko #
#---+---+---+---+---+#

word_list = (input('Enter your sequance of words with "," separators ').split(', '))
word_set: set = set(word_list)
print(sorted(word_set))