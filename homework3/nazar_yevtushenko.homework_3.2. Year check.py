''' Homework #3. Task #2
Made by Nazar Yevtushenko '''

# Input
year = input('Hello! Please state the year of birth(in format 1900 - 2022): ')

# Digit check
while not year.isdigit():
  year = input('Sorry, buy you make a mistake. Please insert year in digit format: ')
year = int(year)

# Range check
while not 1900 <= year <= 2022:
  year = int(input('Please state the year of birth(in format 1900 - 2022): '))


age = 2022 - year
if age == 21:
  print('You should visit Holland')
elif age > 21:
  print('You should visit Vietnam')
else:
  print('Travell everywhere')
