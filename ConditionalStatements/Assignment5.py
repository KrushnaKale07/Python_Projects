#Q1: check if the iterable is empty

# d = {'sport': 'Cricket', 'Mode':'one-day','Target':327, 'overs': 50}
#
# if len(d)==0:
#     print(' d is empty')
# else:
#     print('d is not empty')


#Q2: greatest of 3 numbers
#
# num1 = int(input('Enter 1st number'))
# num2 = int(input('Enter 2nd number'))
# num3 = int(input('Enter 3rd number'))
#
# if num1>num2 and num1>num3:
#     print(f'{num1} is gretest number')
# elif num2>num3 and num2>num1:
#     print(f'{num2} is greatest number')
# else:
#     print(f'{num3} is greatest number')


#Q3: converting upper to lower and vice versa
#
# 1st Way
# char = input('Enter the character')
#
# if len(char)==1:
#     ascii = ord(char)
#     if ascii>=65 and ascii<=90:
#           l_ascii = ascii+32
#           print(f'{char} was in uppercase and successfully converted in lowercase {chr(l_ascii)}')
#     elif ascii>=97 and ascii<=122:
#           u_ascii = ascii-32
#           print(f'{char} was in lowercase and successfuly converted into uppercase {chr(u_ascii)}')
#     else:
#           print('Enter valid character')
# else:
#     print('Enter single character')

# 2nd WAY
# char = input('Enter the character')
#
# if len(char)==1:
#     if char.isupper():
#           print(f'{char} was in uppercase and successfully converted in lowercase {char.lower()}')
#     elif char.islower():
#           print(f'{char} was in lowercase and successfuly converted into uppercase {char.upper()}')
#     else:
#           print('Enter valid character')
# else:
#     print('Enter single character')


# Q4: check if entered character is vowel or not
#
# char = input('Enter the character')
#
# if len(char)==1:
#     if char in 'AEIOUaeiou':
#         print(f"{char} is a vowel")
#     else:
#         print(f'{char} is not a vowel')
# else:
#     print('please enter single character')


# Q5: check if entered character is vowel or not, if it is vowel then create a dictionary with char and its ascii value pair
#
# character = input('Enter the character')
#
# if len(character)==1:
#     if character in 'AEIOUaeiou':
#         d={}
#         d[character]=ord(character)
#         print(d)
#     else:
#         print(f'{character} is not a vowel')
# else:
#     print('Please enter single character')


# Q6: check if the key is present , if present then increment or initialize the value to 1
#
# d = {'Mobile': 'Iphone', }


# Q7: check if the given value is string or not
#
# value = input('Enter the value')
#
# if type(value)==str:
#     print(f'{value} is a string value')
# else:
#     print(f'{value} is not a string')


# Q8: check if the given number is even or odd
#
# num1 = int(input('Enter the number'))
#
# if num1%2==0:
#     print(f'{num1} is even number')
# else:
#     print(f'{num1} is odd number')


# Q9: check whether the string is palindrome or not
#
# string1 = input('Enter the string value')
#
# r_string=string1[::-1]
#
# if string1==r_string:
#     print(f'{string1} is palindrom string')
# else:
#     print(f'{string1} is not a palindrom string')


# Q10: check if the integer is palindrome or not
#
# num = int(input('Enter the number'))
#
# new_num = str(num)
#
# reverse_num = new_num[::-1]
#
# if new_num == reverse_num:
#     print(f'{num} is palindrom number')
# else:
#     print(f'{num} is not a palindrom number')


# Q11: check if the given year is leap year or not
#
# year = int(input('Enter the Year'))
#
# if year%400==0 or year%4==0:
#     print(f'{year} is  leap year')
# else:
#     print(f'{year} is not a leap year')


# Q12 : check if the given character is number or alphabet or special character
#
# value = input('Enter a value')
#
# v_ascii = ord(value)
#
# if (v_ascii>=65 and v_ascii<=90) or (v_ascii>=97 and v_ascii<=122):
#     print(f'{value} is a alphabet')
# elif v_ascii>=48 and v_ascii<=57:
#     print(f'{value} is number')
# else:
#     print(f'{value} is a special character')

# Q13 : check if the given number is perfect square or not
#
# import  math
#
# num = int(input('Enter the number'))
# sqare_root = math.sqrt(num)
#
# if sqare_root.is_integer():
#     print(f'{num} is perfect square.')
# else:
#     print(f'{num} is not a perfect square')


# Q14:check if the entered marks is greater than 35 then print pass, else print fail, if the marks is above 60 print first class
#
# marks = int(input('Enter the marks'))
#
# if marks>60:
#     print('Passed first class with distinction')
# elif marks>35:
#     print('passed')
# else:
#     print('fail')

# Q15: check if the given string is starting with vowel or not
#
# string1 = input('Enter the string')
#
# character = string1[0]
#
# if character in 'AEIOUaeiou':
#     print(f'{string1} is starts with vowel')
# else:
#     print(f'{string1} is not starts with vowel')


# Q16: check if the given string is ending with vowel or not
#
# string1 = input('Enter the string')
#
# character = string1[-1]
#
# if character in 'AEIOUaeiou':
#     print(f'{string1} is ends with vowel')
# else:
#     print(f'{string1} is not ends with vowel')


# Q17: check if the list has even number of elements
#
# list1 = [1,2,3, 1]
#
# if len(list1)%2==0:
#     print('List1 has even number of element')
# else:
#     print('List1 has not even number of element')


# Q18: check the number of keys in the dictionary, if the number is even print the dictionary as it is, else add a new key to make it even and print it
#
# dict1 = {'brand': 'Tata', 'model_name':'punch', 'color':'White'}
#
# if len(dict1)%2==0:
#     print(dict1)
# else:
#     dict1['price'] = 850000
#     print('length of dictionary ksys was in odd number and successfully converten in enven number by adding key',dict1)


# Q19: In a number check whwther the first number is even or odd
#
# num = int(input('Enter the number'))
#
# new_num = str(num)
#
# first_num = new_num[0]
#
# if int(first_num)%2==0:
#     print(f'{first_num} is even number')
# else:
#     print(f'{first_num} is odd number')


# Q20: In a number check if the second last number is even or odd
#
# num = int(input('Enter the number'))
#
# new_num = str(num)
#
# sec_last_num = new_num[-2]
#
# if int(sec_last_num)%2==0:
#     print(f'{sec_last_num} is even number')
# else:
#     print(f'{sec_last_num} is odd number')
