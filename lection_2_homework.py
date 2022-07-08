'''Simplest calk
Homework №2. Python beginer course
Nazar Yevtushenko'''

a = int(input("Insert your first values: ")) #Input first operand
b = int(input("Insert your second values: ")) #Input second operand
print('\nChoose you operators:', '1 = +', '2 = -', '3 = +', '4 = /', '5 = mod', '6 = exp', '7 = floor division', '8 = Equal check', '9 = All results', sep='\n') #Input operators
operand = int(input())
if operand == 1:   #Addition
    print("Addition Result:", a + b)
elif operand == 2: #Substraction
    print("Substraction Result:", a - b)
elif operand == 3: #Multiplication
    print("Multiplication Result:", a * b)
elif operand == 4: #Division
    if b == 0: #Zero check
        print("Result: Devided by ZERO")
    else:
        print("Division Result:", a / b)
elif operand == 5: #Modulus
    print("Modulus Result", a % b)
elif operand == 6: #Exponentiation
    print("Exponentiation Result", a ** b)
elif operand == 7: #Floor division
    print("Floor division Result", a // b)
elif operand == 8: #Equal check
    print("Equal check. Operands are equals: ", a == b )
elif operand == 9: #All results
    print("Addition Result:", a + b)
    print("Substraction Result:", a - b)
    print("Multiplication Result:", a * b)
    print("Division Result:", a / b)
    print("Modulus Result", a % b)
    print("Exponentiation Result", a ** b)
    print("Floor division Result", a // b)
    print("Equal check. Operands are equals: ", a == b )
else:
    print("Undefined operation")