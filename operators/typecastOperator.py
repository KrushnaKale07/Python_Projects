# Typecasting for Individual datatypes

# a=1.3334556
# print(int(a))
#
# b= 10
# print(float(b))
#
# c = True
# print(float(c))

# Typecasting for collection datatypes
# list into set, tuple, string, dictionary
#
# l=[1,3,4,5]
# print(set(l))
# # {1, 3, 4, 5}
#
# print(tuple(l))
# # (1, 3, 4, 5)
#
# print(String(l))
# NameError: name 'String' is not defined
#
# print(dict(l))
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

# typecast set into list,tuple,string,dictioary
#
# s={True, 12, 'Kale', 15.5}
# print(list(s))
# # [True, 'Kale', 12, 15.5]
#
# print(tuple(s))
# # ('Kale', True, 12, 15.5)
#
# print(str(s))
# {True, 'Kale', 12, 15.5}
#
# print(dict(s))
# {'Kale', True, 12, 15.5}

# dict into list,set,tuple,String
#
# d={'name':'Krushna', 'id': 12, 'age' : 23}
#
# print(list(d))
# # ['name', 'id', 'age']
#
# print(set(d))
# # {'name', 'id', 'age'}
#
# print(tuple(d))
# # ('name', 'id', 'age')
#
# print(str(d))
# # {'name': 'Krushna', 'id': 12, 'age': 23}

# tuple into list,set,dict,String
#
# t=(12,True,'Yash',18.89)
# print(set(t))
# # {'Yash', True, 18.89, 12}
#
# print(list(t))
# # [12, True, 'Yash', 18.89]
#
# # print(dict(t))
# # TypeError: cannot convert dictionary update sequence element #0 to a sequence
#
# print(str(t))
# (12, True, 'Yash', 18.89)

# String into list,set,dictionary, tuple
#
# string1 = 'Good morning pune'
#
# print(list(string1))
# ['G', 'o', 'o', 'd', ' ', 'm', 'o', 'r', 'n', 'i', 'n', 'g', ' ', 'p', 'u', 'n', 'e']
#
# print(set(string1))
# {'p', 'm', 'n', 'i', 'd', 'u', 'e', 'o', 'G', ' ', 'g', 'r'}
#
# print(dict(string1))
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
#
# print(tuple(string1))
# ('G', 'o', 'o', 'd', ' ', 'm', 'o', 'r', 'n', 'i', 'n', 'g', ' ', 'p', 'u', 'n', 'e')
