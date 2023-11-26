char = input('Enter the character')

if len(char)==1:
    if char.isupper():
          print(f'{char} was in uppercase and successfully converted in lowercase {char.lower()}')
    elif char.islower():
          print(f'{char} was in lowercase and successfuly converted into uppercase {char.upper()}')
    else:
          print('Enter valid character')
else:
    print('Enter single character')
