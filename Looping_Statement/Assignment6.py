#Q1: Print numbers from 0 to 4 (upto 5 but not including 5)
#
# for i in range(0,5):
#     print(i,end=" ")
# # 0 1 2 3 4


# Q2: Print numbers from 1 to 4 (num starts from zero if start index is omitted)
#
# for i in range(1,5):
#     print(i,end=" ")
# # 1 2 3 4


# Q3: Print every alternate numbers starting zero
#
# for i in range(0,10,2):
#         print(i,end=" ")
# # 0 2 4 6 8


#Q4: Print number from 10 to 1
#
# for i in range(10,0,-1):
#         print(i,end=" ")
# # 10 9 8 7 6 5 4 3 2 1


#Q5: Print number form 10 to 0
#
# for i in range(10,-1,-1):
#         print(i,end=" ")
# # 10 9 8 7 6 5 4 3 2 1 0


# Q6: Print alternate numbers from 10 to 0
#
# for i in range(10,-1,-2):
#         print(i,end=" ")
# # 10 8 6 4 2 0


# Q7: Print "Python is awesome!!" 5 times
#
# for i in range(1,6):
#         print("Python is awesome!!")
# #Python is awesome!!
# # Python is awesome!!
# # Python is awesome!!
# # Python is awesome!!
# # Python is awesome!!


# Q8: Print numbers from -10 to -1
#
# for i in range(-10,0):
#         print(i,end=" ")
# # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


# Q9: Print numbers from 10 to -1
#
# for i in range(10,-2,-1):
#     print(i,end=" ")
# # 10 9 8 7 6 5 4 3 2 1 0 -1


# Q10: Print even numbers from 1 to 10
#
# for i in range(1,11):
#     if i%2==0:
#         print(i,end=" ")
# # 2 4 6 8 10


# Q11: Print odd  numbers
#
# for i in range(1,11):
#     if i%2!=0:
#         print(i,end=" ")
# # 1 3 5 7 9


# Q12: Iterate over the list only if the list has atleast 1 item.
# l = [[1, 2, 3], [], ["hai"]]
# for i in l:
#     ele = len(i)
#     if ele>=1:
#         print(i,end=" ")
# # [1, 2, 3] ['hai']


# Q13: Iterate over the list only if the string has atleast 1 item.
#
# l = ["hi", "There", "How", "Are", "You", "All", "Have", "A", "Nice", "Day"]
#
# for i in l:
#     ele = len(i)
#     if ele>=1:
#         print(i,end=" ")
# # hi There How Are You All Have A Nice Day


# Q14: Iterate over the list only if the dictionary has atleast 1 item.
#
# l = [{'sport' : 'cricket', 'Players': '11'},{},{'langauge':'Python'}]
#
# for i in l:
#     ele = len(i)
#
#     if ele>=1:
#         print(i)
# # {'sport': 'cricket', 'Players': '11'}
# # {'langauge': 'Python'}


# Q15: Iterate over the list only if the set has atleast 1 item.
#
# l = [{'ksk',12},{'er',True},{}]
#
# for i in l:
#     ele = len(i)
#
#     if ele>=1:
#         print(i)
# # {'ksk', 12}
# # {True, 'er'}


# Q16:Iterate over the list only if the tuple has atleast 1 item.
#
# l=[(1,2,3),(),(True,False),('Ksk','Kjei'),(),()]
#
# for i in l:
#     ele = len(i)
#
#     if ele>=1:
#         print(i)
# # (1, 2, 3)
# # (True, False)
# # ('Ksk', 'Kjei')


# Q17: Find the sum of first 10 even numbers
#
# sum = 0
# for i in range(1,21):
#     if i%2==0:
#         sum += i
# print(sum)
# # 110


# Q18: Write a program to print prime numbers from 1 to 50
#
# for i in range(1,51):
#     for j in range(1,51):
#         if i%j==0 and i%1==0:
#             print(i)
#

# Q19: Program to convert uppercase characters to lowercase characters
# and lowercase characters to uppercase characters in the string
#
# String1 = "Hello KrUsHna"
# for i in String1:
#     ascii_value = ord(i)
#
#     if ascii_value>=65 and ascii_value<=90:
#         lower =i.lower()
#         print(lower)
#     elif ascii_value>=97 and ascii_value<=122:
#         upper = i.upper()
#         print(upper)
#     else:
#         print()

# Q20: Program to convert lowercase characters to uppercase characters in the string
#
# String1 = "hello krushna"
# for i in String1:
#     ascii_value = ord(i)
#     if ascii_value>=97 and ascii_value<=122:
#         upper = i.upper()
#         print(upper,end=' ')

# Q21: Program to convert uppercase characters to lowercase characters in the string
#
# String1 = "HELLO KRUSHNA"
# for i in String1:
#     ascii_value = ord(i)
#
#     if ascii_value>=65 and ascii_value<=90:
#         lower =i.lower()
#         print(lower,end=" ")

# Q22: Program to print only integer datatypes in the list
#
# l = [ "hi", "hello", 10, "12.3", 12, 90, 6.2]
#
# for i in l:
#     if type(i)==int:
#         print(i)


# Q23: Program to print only integer and float datatypes in the list
#
# l = [ "hi", "hello", 10, "12.3", 12, 90, 6.2]
#
# for i in l:
#
#     if type(i)==int or type(i)==float:
#         print(i)

# Q24: program to print all the numeric values in the list
#
# l = [ "hi", "hello", 10, "12.3", 12, 90, 6.2]
#
# for i in l:
#     # if l.isdigit(i):
#     #     print(i)
#     # elif type(i) in [int,float]:
#
#     if type(i) in [int,float]:
#         print(i)

# Q25: Program to print only vowels in the string "Python selenium"
#
# s = "Python selenium"
#
# for i in s:
#     if i in 'AEIOUaeiou':
#         print(i)

# Q26: Program to print only consonants in the string "Python selenium"
#
# s = "Python selenium"
#
# for i in s:
#     if i not in 'AEIOUaeiou':
#         print(i)

# Q27: Program to print all the square numbers in the list.
#
# nums = [10, 25, 4, 56, 64, 256]
#
# for i in nums:
#     square_root = i ** 0.5
#     if square_root.is_integer():
#         print(i)


# Strings

# Q1: Iterating over string using range function.
#
# s = "hello world"
#
# for i in s:
#     print(i)

# Q2: iterating over a string in reversed direction
#
# s = "hello world"
# print(s[::-1])


# Q3:Printing Index and Character using range class

# s = "hello world"
#
# for val1 in enumerate(s):
#     print(val1)


# Q4: Iterating over multiple string objects using zip class
#
# s1 = "Hello"
# s2= "Krushna"
#
# for val1,val2 in zip(s1,s2):
#     print(val1,val2)

# Q5: Printing alternate characters of the string
#
# s1 = "Krushna Kale"
#
# print(s1[::2])


# Q6: Program to count the number of digits and alphabets in the string "hai 1234 python23"
#
# s1 = "hai 1234 python23"
# alpha_count = 0
# digit_count = 0
#
# for i in s1:
#     if i.isalpha():
#          alpha_count+=1
#     elif i.isdigit():
#         digit_count+=1
#
# print(f'Alpha_count is {alpha_count}')
# print(f'Digit count is {digit_count}' )

# Q7: Program to count the number of capital and small letters in the string "HelLo WORld"
#
# s1 = "HelLo WORld"
# capital_count = 0
# small_count = 0
#
# for i in s1:
#     if i.islower():
#         small_count+=1
#     elif i.isupper():
#         capital_count+=1
#
# print(f'Capital count is {capital_count}')
# print(f'Small count is {small_count}')



# Lists

# Q1: Prints the item and its corresponding index in the list
#
# l = ["a", "b", "c","d"]
#
# for value in enumerate(l):
#     print(value)


# Q2: Printing alternate items of the list
#
# l = ["a", "b", "c","d"]
# print(l[::2])

# Q3: Iterating over multiple lists simultaneously
#
# l1 = ["a", "b", "c","d"]
# l2 = [1,2,3,4]
#
# for val1, val2 in zip(l1,l2):
#     print(val1,val2)

# Q4: Iterating through multiple list with un-equal lengths using zip class

# l1 = ["a", "b", "c","d"]
# l2 = [1,2,3,4,5,6,7,8,9]
#
# for val1, val2 in zip(l1,l2):
#     print(val1,val2)

# Q5: Program to print filenames ending with pdf.
#
# files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
# l=[]
# for i in files:
#     extension = i.split('.')
#     if extension[1] == 'pdf':
#         l.append(i)
# print(l)


# # Q7: Print the extension of each file name in the list
#
# files = ['youtube.txt', 'yahoo.pdf', 'microsoft.doc', 'apple.xls', 'amazon.xml']
# for i in files:
#     extension = i.split('.')
#     print(extension[1])

# Q9: Program to print the length of each word in the list
#
# files = ['youtube','txt', 'yahoo','pdf', 'microsoft','doc', 'apple','xls', 'amazon','xml']
#
# for i in files:
#     print(len(i))

# Q10: Program to print the length of each word in the list in the form of tuples
#
# files = ['youtube','txt', 'yahoo','pdf', 'microsoft','doc', 'apple','xls', 'amazon','xml']
# t=[]
# for i in files:
#     length = len(i)
#     t[i]=length
#
# print(t)


# Dictionary
#
#
# Q1:Print only keys of the dictionary
#
# d = {'num1' : 1, 'num2': 2, 'num3' : 3}
# print(d.keys())


#Q2: Print Values of the dictionary
#
# d = {'num1' : 1, 'num2': 2, 'num3' : 3}
# print(d.values())


#Q3: Print index and item of the dictionary
#
# d = {'num1' : 1, 'num2': 2, 'num3' : 3}
# for i in enumerate(d):
#     print(i)


#Q4: Count number of words in a sentence using get method
#
# s1 = 'hello world hello world welcome to python'
# l1 = s1.split(' ')
# count = 0
# for i in l1:
#     if len(i)>0:
#         count+=1
# print(f'Count of words in sentence is = {count}')


#Q5: Counting number of characters in a string
# count = 0
# s = 'abracadabraca'
# for i in s:
#     if len(i)>0:
#         count+=1
# print(f'Count of characters in string is = {count}')


#Q6: Counting number of vowels in a string
#
# sentence = "hello world welcome to python hello hi hello hello"
#
# count = 0
# for i in sentence:
#     if i in 'AEIOUaeiou':
#         count+=1
# print(f'Count of vowels in string is = {count}')

#Q7: Counting occurances of word in the string
#
# sentence = "hello world welcome to python hello hi hello hello"
#
# count = 0
# for i in sentence:
#     if i not in 'AEIOUaeiou':
#         count+=1
# print(f'Count of vowels in string is = {count}')


#Q8: Counting occurances of each character in the string
#
# s = 'abracadabraca'
# d = {}
# index = 0
# while index<len(s):
#     char = s[index]
#     if char in d:
#         d[char]+=1
#     else:
#         d[char]=1
#     index+=1
# print(d)
# # {'a': 6, 'b': 2, 'r': 2, 'c': 2, 'd': 1}

#Q9: Create a dictionary for the below list
# cities = [('India', ' Bangalore '),
#           ('India', ' Chennai '),
#           ('India', ' Delhi '),
#           ('India', ' Kolkata '),
#           ('USA', ' Dallas '),
#           ('USA', ' New York '),
#           ('USA', ' Chicago '),
#           ('China', ' Beijing '),
#           ('China', ' Shanghai ')
#           ]
#
# d ={}
# for element in cities:
#     country = element[0]
#     city = element[-1]
#
#     if country in d:
#         d[country]+=city
#     else:
#         d[country]=city
# print(d)

#Q10: Adding items of two lists corresponding to their indices
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
#
# l=[]
# for i in zip(a,b):
#     l[] =
# print(l)

#Q11: flattening the list using Multiple "for" loops
# items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l=[]
#
# for i in items:
#     for j in i:
#         l.append(j)
# print(l)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Q12: Python Program for 100 Fibonacci number
# a = 1
# b = 0
# while b<=100:
#     c = a + b
#     a = b
#     b = c
#     print(c)


#Q13: Python Program for Sum of squares of first 100 natural numbers
#
# a = 1
# c = 0
# while a<=100:
#     b = a**2
#     c += b
#     a+=1
# print(c)
# # 338350


#Q14: Python Program for cube sum of first n natural numbers
#
# a = 1
# c = 0
# while a<=100:
#     b = a**3
#     c += b
#     a+=1
# print(c)
# # 25502500
