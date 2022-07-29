#---+---+---+---+---+#
# Homework #4. Task 1#
#  Nazar Yevtushenko #
#---+---+---+---+---+#
def filo(str):
    if len(str) <= 2:
        print(f'Sting is very short. Please, insert again - {str}')
    else:
        print(str[:2]+str[-2:])

filo(input('Insert your string '))
