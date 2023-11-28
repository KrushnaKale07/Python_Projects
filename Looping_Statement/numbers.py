# Print 1 to 10 number in increament order
# for number in range(1,11):
#     print(number, end=' ')
# print()


# Print 1 to 10 number in decreament order
#
# for number in range(10,0,-1):
#     print(number, end=' ')
# print()

# WAP to print even and odd number between 1 to 100
# Even

# one way
# for number in range(1,101):
#     if number%2==0:
#         # print(f'{number} is even number')
#         print(number,end=' ')
# print()

# second way
# for number in range(2,101,2):
#     print(number, end=' ')

# Odd
# one way
# for number in range(1,101):
#     if number%2!=0:
#         print(number,end=' ')

# 2nd Way
#
# for number in range (1,101,2):
#     print(number,end=' ')

# WAP to print addition of even number in 1 to 10
#
# sum=0
# for number in range(1,11):
#     if number%2==0:
#         sum+=number
#
# print(f' Sum of even number of 1 to 10 {sum}')

# 2nd Way
# sum=0
# for number in range(2,11,2):
#         sum+=number
#
# print(f' Sum of even number of 1 to 10 = {sum}')

# Wap to print addition of odd number in 1 to 10
#
# sum=0
# for number in range(1,11):
#     if number%2!=0:
#         sum+=number
#
# print(f'Sum of odd number of 1 to 10 = {sum}')

# 2nd way

# sum=0
# for number in range(1,10,2):
#         sum+=number
#
# print(f'Sum of odd number of 1 to 10 = {sum}')

# WAP to print all uppercase and lowercase character
#
# # for uppercase in range(65,91):
# #     print(chr(uppercase),end=' ')
#
# for lowercase in range(97,123):
#     print(chr(lowercase),end=' ')

# in a reverse way
#
# for uppercase in range(90,64,-1):
#     print(chr(uppercase),end=' ')
#
# for lowercase in range(122,96,-1):
#     print(chr(lowercase),end=' ')

# WAP to print lowercase character into uppercase character and uppercase character into lowercase character of given string
#
# string1 = input('Enter the string')
# new_string = ''
#
# for index in range(0,len(string1)):
#     char = string1[index]
#     askii = ord(char)
#
#     if askii in range(65,91):
#         l_askii = askii+32
#         new_string += chr(l_askii)
#     elif askii in range(97,123):
#         u_askii = askii-32
#         new_string += chr(u_askii)
#     else:
#         new_string=char
# print(new_string)
