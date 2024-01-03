# list and set Comprehensions
# -----------------

#Q1: Square Numbers in the list. Using List Comprehensions
#
# list=[1,2,3,4]
# l=[]
# for i in list:
#     l.append(i**2)
# print(l)
# [1, 4, 9, 16]

# Using list Comprehension
# l = [ i**2 for i in list ]
# print(l)
# # [1, 4, 9, 16]


#Q2: List of even numbers between range 1-50
#
# l=[i for i in range(1,51) if i%2==0]
# print(l)
# # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
#Q3: Returns a list names starting with vowels in the given string
#
# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# l=[ i for i in names if i[0] in 'AIOEUaeiou']
# print(l)
# # ['alex', 'ive']

#Q4: Filtering all the languages which starts with 'p'
#
# languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
# l = [i for i in languages if i.startswith('P')]
# print(l)
# # ['Python', 'Perl', 'PHP', 'Python', 'Python']

#Q5: Names starting with consonants
#
# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# l=[ i for i in names if i[0] not in 'AIOEUaeiou']
# print(l)
# # ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott']

#Q6 Filtering out those names which are less than 6 characters
# names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
# l=[i for i in names if len(i)<6]
# print(l)
# # ['apple', 'yahoo', 'gmail']

#Q7 Raise to the power of list index
# a = [1, 2, 3, 4, 5]
# result = [i ** index for index, i in enumerate(a)]
# print(result)
# # [1, 2, 9, 64, 625]

#Q8: Build a list of tuples with string and its length pair
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l=[(i, len(i)) for i in names]
# print(l)
# [('apple', 5), ('google', 6), ('yahoo', 5), ('facebook', 8), ('yelp', 4), ('flipkart', 8), ('gmail', 5), ('instagram', 9), ('microsoft', 9)]

#Q9: Build a list with only with even length string
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l=[i for i in names if len(i)%2==0]
# print(l)
# # ['google', 'facebook', 'yelp', 'flipkart']

# Q10: Generating List of PI values
# o/p: [3.0, 3.1, 3.14, 3.141]

#Q11: List comprehension to sum the factorial of numbers from 1-5
sum = 0;
for i in range(1,6):
    for j in range(1,6):
        if i%j==0:
            sum+=j

# l=[j for i in range(1,6) for j in range(1,6) if i%j==0 ]
print(sum)


#Q12: Reverse the item of a list if the item is of odd length string
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l=[]
# for i in names:
#     if len(i)%2!=0:
#         l.append(i[ : :-1])
# print(l)
# # ['elppa', 'oohay', 'liamg', 'margatsni', 'tfosorcim']
#
# l=[i[::-1] for i in names if len(i)%2!=0]
# print(l)
# # ['elppa', 'oohay', 'liamg', 'margatsni', 'tfosorcim']


# #13: Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l=[i[::-1] if len(i)%2!=0 else i for i in names]
# print(l)
# # ['elppa', 'google', 'oohay', 'facebook', 'yelp', 'flipkart', 'liamg', 'margatsni', 'tfosorcim']

#Q14: Reverse the string if the string is of odd length, otherwise keep it as is.
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l=[i[::-1] if len(i)%2!=0 else i for i in names]
# print(l)
# # ['elppa', 'google', 'oohay', 'facebook', 'yelp', 'flipkart', 'liamg', 'margatsni', 'tfosorcim']

# Dictionary Comprehensions
# ---------------
#Q1: Building a dict of word and length pair
# words = "This is a bunch of words"
# d={i:len(i) for i in words.split(' ')}
# print(d)
# # {'This': 4, 'is': 2, 'a': 1, 'bunch': 5, 'of': 2, 'words': 5}

#Q2: Flipping keys and values of the dictionary using dict comprehension
# d = {'a': 1, 'b': 2, 'c': 3}
# d1={value:key for key,value in d.items()}
# print(d1)
# # {1: 'a', 2: 'b', 3: 'c'}

#Q3: Counting the number of each character in a String
# my_string = 'guido van rossum'
# d={i:my_string.count(i) for i in my_string if i.isalpha()}
# print(d)
# # {'g': 1, 'u': 2, 'i': 1, 'd': 1, 'o': 2, 'v': 1, 'a': 1, 'n': 1, 'r': 1, 's': 2, 'm': 1}

#Q4: Counting the number of each character in a String
# sentence = "hello world welcome to python hello hi world welcome to python"
# d={}
# for i in sentence:
#     if i.isalpha():
#         d[i]=sentence.count(i)
# print(d)
# # {'h': 5, 'e': 6, 'l': 8, 'o': 10, 'w': 4, 'r': 2, 'd': 2, 'c': 2, 'm': 2, 't': 4, 'p': 2, 'y': 2, 'n': 2, 'i': 1}

# d1={i:sentence.count(i) for i in sentence if i.isalpha()}
# print(d1)
# # {'h': 5, 'e': 6, 'l': 8, 'o': 10, 'w': 4, 'r': 2, 'd': 2, 'c': 2, 'm': 2, 't': 4, 'p': 2, 'y': 2, 'n': 2, 'i': 1}

#Q5: Dictionary of character and ascii value pairs
# s = 'abcABC'
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)
# # {'a': 97, 'b': 98, 'c': 99, 'A': 65, 'B': 66, 'C': 67}
#
# d={i:ord(i) for i in s}
# print(d)
# {'a': 97, 'b': 98, 'c': 99, 'A': 65, 'B': 66, 'C': 67}

#Q6: Creating Dictionary of city and population pairs using Dict Comprehension
# cities = ['Tokyo',
#           'Delhi',
#           'Shanghai',
#           'Sao Paulo',
#           'Mumbai'
#           ]
# population = ['38,001,000',
#               '25,703,168',
#               '23,740,778',
#               '21,066,245',
#               '21,042,538'
#           ]
# d={}
# for i,j in zip(cities,population):
#    d[i]=j
# print(d)
# # {'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778', 'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}
#
# d={i:j for i,j in zip(cities,population)}
# print(d)
# # {'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778', 'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}


#Q7: Create a dictionary of dialcode and country from the following list
# dial_codes = [
#     (86, 'China'),
#     (91, 'India'),
#     (1, 'United States'),
#     (62, 'Indonesia'),
#     (55, 'Brazil'),
#     (92, 'Pakistan'),
#     (880, 'Bangladesh'),
#     (234, 'Nigeria'),
#     (7, 'Russia'),
#     (81, 'Japan')
#     ]
#
# d={}
# for i in dial_codes:
#     d[i[1]]=i[0]
# print(d)
# {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
#
# d={i[1]:i[0] for i in dial_codes}
# print(d)
# # {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}

#Q8: Building a dictionary whose price value is more than 200
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# d = {i: j for i, j in prices.items() if j > 200}
# print(d)
# # {'AAPL': 612.78, 'IBM': 205.55}


# sum = 0
# for i in range(1,21):
#     if i%2!=0:
#         sum+=i
# print(sum)

# for i in range(10,0,-1):
#     print(i)

# print("odd numbers are")
# for i in range(1,101):
#     if i%2==0:
#         print(f'{i},end=" ")

# print("even numbers are")
# for i in range(2,101,2):
#         print(f'{i}',end=" ")

# for i in range(65,91):
#     print(chr(i),end=" ")

# for i in range(97,122):
#     print(chr(i),end=" ")

# string = input("")
# new_str = ""
#
# for i in range(0,len(string)):
#     char = string[i]
#     ascii = ord(char)
#
#     if ascii in range(65,91):
#         lower_ascii = ascii+32
#         new_str += chr(lower_ascii)
#     elif ascii in range(97,123):
#         upper_case = ascii-32
#         new_str += chr(upper_case)
#     else:
#         new_str+=char
# print(f'ald string was {string} is converted in {new_str}')


# d = {'name' : 'steve','age' : 12}
# key = input("Enter the Key")
# if key in d:
#     if type(d[key]) in [int,float]:
#         d[key]+=1
#         print(f'the updated increament value of key is {d[key]}')
#     else:
#         d[key]=1
#         print(f'the reinitialize of {key} is {d[key]}')
# else:
#     print('key is not present')

# s = 'Hello world Hello world welcome to python'
#
# list = s.split(' ')
# d={}
#
# for i in list:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
