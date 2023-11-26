# Q: WAP to convert uppercase character into lowercse character and lowercase character into uppercase character

char = input('Enter the character')

if len(char)==1:
    ascii = ord(char)
    if ascii>=65 and ascii<=90:
          l_ascii = ascii+32
          print(f'{char} was in uppercase and successfully converted in lowercase {chr(l_ascii)}')
    elif ascii>=97 and ascii<=122:
          u_ascii = ascii-32
          print(f'{char} was in lowercase and successfuly converted into uppercase {chr(u_ascii)}')
    else:
          print('Enter valid character')
else:
    print('Enter single character')
