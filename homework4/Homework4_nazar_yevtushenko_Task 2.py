#---+---+---+---+---+#
# Homework #4. Task 2#
#  Nazar Yevtushenko #
#---+---+---+---+---+#


main_str = (input("Insert your string: "))
main_dic = {}

for letter in main_str:
    main_dic[f'{letter}'] = main_str.count(letter)

print(main_dic)