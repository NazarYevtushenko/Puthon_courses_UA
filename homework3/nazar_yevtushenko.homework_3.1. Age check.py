''' Homework #3. Task #1
Made by Nazar Yevtushenko '''

# Ask input date of client
name = input('Hello! Please, enter you name: ')
age = int(input(f'Thank you {name}. Enter your age: '))

#Age check
if age == 16:
  print(f'Dear {name} need to wait one year.')
elif age > 16:
  if 70<=age<=90:
      print(f'You are lucky {name} and welcome.')
  elif age > 121:
      print(f'You are not real {name}.')
  else:
      print(f'Welcome {name} on our website.')
else:
  print(f"I'm sorry {name}")