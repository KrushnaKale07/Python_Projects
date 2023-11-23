# str1 = 'hello everyone good morning, have nice day'
# print("string 1 = ", str1)
# print()
#
# str2 = 'HELLO EVERYONE GOOD MORNING, HAVE NICE DAY'
# print("string 2 = " ,str2)
# print()

# Q1: WAP to convert uppercase string into lowercase string and lowercase into uppercase

# print(" Lowercase String converted into uppercase = ",str1.upper())
# //HELLO EVERYONE GOOD MORNING, HAVE NICE DAY

# print("Lowercase String converted into uppercase = ", str2.lower())
# //hello everyone good morning, have nice day

# Q2: WAP to check whether the string is starting with substring or ending with substring

# print(str1.startswith('hel'))
# //True
# print(str1.startswith('el'))
# //False


# print(str1.endswith('day'))
# //True
# print(str1.endswith('da'))
# //false

# Q3: WAP to remove LHS and RHS white spaces from given string

# str3 = '     good night     '
# print(str3.strip())
# //good night

# Q4: WAP to print string in reverse order

# str4 = 'hello everyone good morning, have nice day'
# print(str4)
# print()
# print(str4[::-1])
# //yad ecin evah ,gninrom doog enoyreve olleh

# Q5: WAP to print string in reverse alternate order

# str5 = 'hello everyone good morning, have nice day'
# print(str5)
# print()
# print(str5[::-2])
# //ydei vh,nno ogeorv le

# Q6: WAP to print string in alternate order

# str6 = 'hello everyone good morning, have nice day'
# print(str6)
# print()
# print(str6[::2])

# Q7: WAP to split a string on the basis of your requirement

# str7 = 'hello everyone good morning, have nice day'
# print(str7.split('o'))
# //['hell', ' every', 'ne g', '', 'd m', 'rning, have nice day']

# Q8: WAP to count pattern in a string

# str8 = 'hello everyone good morning, have nice day'
# print(str8.count('o'))
# //5

# Q9: WAP to count length of every collection datatypes

# list1 = [1,2,3,4,5,6]
# print(len(list1))
# //5

# set1 = {1,1.2,True,'raj',False,}
# print(len(set1))
# //4

# dict1 = {'name' : 'john', 'id': 1, 'age' : 22, 'dob' : '06/11/2000'}
# print(len(dict1))
# //4

# str9 = 'hello everyone good morning, have nice day'
# print(len(str9))
# //42

# Q10 : WAP to replace a substring with new substring

# str10 = 'hello everyone good morning, have nice day'
# print("Original string = ",str10)
# //Original string =  hello everyone good morning, have nice day
# print()

# print("Replaced string = ",str10.replace('nice','good'))
# Replaced string =  hello everyone good morning, have good day
