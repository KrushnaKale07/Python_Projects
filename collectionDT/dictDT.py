# Dictionary

d = {'name':'Raja', 'age' : 12}
# print(d['age'])
# # //12
# print(d['salary'])
# //KeyError: 'salary'

# get method
# it is use to access value of perticular key from dictionary

# print(d.get('age'))
# //12
# print(d.get('agee'))
# //None

# pop method
# it is use to get speficic value from dictionary

# print(d.pop('name'))
# //Raja
# print(d.pop('namee'))
# KeyError: 'namee'

# popitem method
# it is use to get lagt value from dictionary
# d.popitem()

# print(d)
# {'name': 'Raja'}
# print(d.popitem())
# ('age', 12)

# copy method
# it is use to copy element from one dictionary to another dictionary

# var = d.copy()
# print(var)
# {'name': 'Raja', 'age': 12}

# clear method
# it is use to delete all elements from dictionary

# d.clear()
# print(d)

# keys method
# it is use to get all keys from dictionary

# print(d.keys())
# dict_keys(['name', 'age'])

# values method
# it is use to get all values from dictionary

# print(d.values())
# dict_values(['Raja', 12])
