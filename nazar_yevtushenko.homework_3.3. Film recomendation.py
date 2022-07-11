''' Homework #3. Task #3
Made by Nazar Yevtushenko '''

#input
name = input('Hello everybody! What is your name? ')

# Gender
sex = input(f'Good to see you, {name}. what is your gender? (In format M or F) ')
# Gender check
sex_check = {'M', 'F', 'm', 'f'}
while sex not in sex_check:
  sex = input('Please, insert your gender correctly?(In format M or F) ')

# Age input
age = input("Please enter your age in digit format: ")
# Age check
while not age.isdigit():
  age = input("Please enter your age correctly in digit format: ")
# Admin check
age = int(age)
ad = 'admin'
while name == ad:
  print('Привет, повелитель!')
  break
  
if name == 'Женя':
  print("Советую Вам посмотреть 'TENET'")
else:
  if sex == 'M' or sex == 'm':
    if 10 <= age <= 14 or age > 30:
      print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'")
    elif age < 10:
      print("Советую Вам посмотреть 'TMNT'")
  else:
    if age < 16:
      print("Советую Вам посмотреть 'Инсургент'")
    elif 22 <= age <= 32:
      print("Советую Вам посмотреть 'Трансформеры'")
    else:
      print("Иди на кухню готовить")
if name == "Guido":
  print("Огромное спасибо!")