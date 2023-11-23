# String immutable collection datatype

# upper method
# it is use to convert lowercase string in uppercase string

# str1 = 'krushna123'
# print(str1)
# print(str1.upper())
# str2 = str1.upper()
# print(str2)
# KRUSHNA123

# lower method
# it is use convert uppercase string in lowercase string

# str1 = 'KRUSHNA123'
# print(str1)
# print(str1.lower())
# str2 = str1.lower()
# print(str2)
# krushna123

# startswith method
# it is use to check whether string is starts with character or substring

# str1 = 'hello krushna'
# print(str1.startswith('he')) //True
# print(str1.startswith('kru')) //False

# endswith method
# it is use to check whether a given string ends with character or sbstring

# str1 = 'hello krushna'
# print(str1.endswith('hna')) //True
# print(str1.endswith('kru')) //False

# strip method
# it is use to delete white spaces from both side of string

# str1 = '    hello krushna    '
# print(str1.strip())
# // hello krushna


# lstrip method
# it is use to delete LHS white spaces of string

# str1 = '    hello krushna    '
# print(str1.lstrip())
# //hello krushna

# rstrip method
# it is use to delete RHS white spaces of strig

# str1 = '    hello krushna    '
# print(str1.rstrip())
# //    hello krushna

# slicing
# it is use to extracting a perticular character or substring for our requirement

# str1 = 'Hello everyone good morning, have nice day'
# print(str1[4::])
# //o everyone good morning, have nice day
# print()
#
# print(str1[:7:])
# //Hello e
# print()
#
# print(str1[::9])
# //Hrd,c
# print()
#
# print(str1[4:8:])
# //o ev
# print()
#
# print(str1[:8:2])
# //Hloe
# print()
#
# print(str1[4::3])
# //ovyeo rn vnea
# print()
#
# print(str1[6:14:1])
# //everyone

# split method
# it is use to split string as per our requirement

str1 = 'Hello everyone good morning, have nice day'
print(str1)

# print(str1.split(' '))
# //['Hello', 'everyone', 'good', 'morning,', 'have', 'nice', 'day']

# print(str1.split('o'))
# //['Hell', ' every', 'ne g', '', 'd m', 'rning, have nice day']


# count method
# it is use to count perticular character or perticular pattern of a substring in a strig

# print(str1.count('o'))
# //5

# print(str1.count('he'))
# //0

# len method
# it is use to check a length of perticular iteranble object

# print(len(str1))
# //42

# replace method
# it is use to to replace old substring with new substring

# print(str1.replace('nice', 'good'))
# //old substring = Hello everyone good morning, have nice day
# //new substring = Hello everyone good morning, have good day

