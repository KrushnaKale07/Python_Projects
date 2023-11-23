# LIST
# List can accept hetrogenous type of data

# li = [12, 'String', 12.22, True, 'String', []]
# print('original List is')
# print(li)
# # //[12, 12.22, True, 'String', []]
# print()

# append()
# it is use to add element in the list at the last

# li.append('Kale')
# print('Using append method')
# print(li)
# //[12, 12.22, True, 'String', [], 'Kale']
# print()

# insert(index, Value to be added)
# it is use to add value at specific position

# print('Using insert method')
# li.insert(3,False)
# print(li)
# //[12, 12.22, True, False, 'String', []]
# print()

# li.insert(9,'Raja')
# print('Using insert method')
# //[12, 12.22, True, 'String', [], 'Raja']
# print(li)
# print()

# extend([])
# it is use to add more than one value

# We can add list
# li.extend([1,False,'Kale'])
# print('Adding list using extend method')
# print(li)
# //[12, 12.22, True, 'String', [], 1, False, 'Kale']
# print()

# We can add set.
# li.extend({1,12.32,'Ram',True})
# print('Adding Set using extend method')
# print(li)
# //[12, 12.22, True, 'String', [], 1, 'Ram', 12.32]
# print()

# pop()
# it is use to remove element from specific index

# print('only Pop() method will delete last index value')
# print(li.pop())
# //[]

# print('Pop(index) method will delete value present in that index')
# print(li.pop(0))
# // 12
# print()

# print(li.pop(15))
# // IndexError: pop index out of range
# print()

# remove()
# it is use to remove specific value from list
# this method accepts value as an argument

# print('Using remove() method')
# var = li.remove('String')
# print(li)
# //[12, 12.22, True, 'String', []]
# print(var)
# //None

# if we try to remove value from list which is not present in that list then it will give us an error
# li.remove('hello')
# print(li)
# //ValueError: list.remove(x): x not in list

# clear()
# it is use to delete all the element from the list

# li.clear()
# print('Using clear() method')
# print(li)
# //[]

# We can access element from the list using index value
# print(li[2])

# print(li[10])
# //IndexError: list index out of range

# copy()
# it is use to copy the whole list

# print('Using copy method')
# print(li.copy())
# [12, 'String', 12.22, True, 'String', []]
# var = li.copy()
# print(var)
# //[12, 'String', 12.22, True, 'String', []]

# reverse()
# it is use to reverse a list

# print('Using reverse method')
# li.reverse()
# print(li)
# //[[], 'String', True, 12.22, 'String', 12]

# sort()
# it is use to sort the element in asending order to desending order

# print('Using sort method')
# li.sort()
# print(li)
# original List is
# [12, 'String', 12.22, True, 'String', []]
# Using sort method
# TypeError: '<' not supported between instances of 'str' and 'int'
# we cant sort list which consisting string and int datatype in it

# to sort list we have element of same datatype else we got error
# li1 = [ 'kale', 'mahesh', 'pradeep', 'ashok', 'seema', 'krushna','rohini']
# li1.sort()
# print(li1)

# li2=[True, False]
# li2.sort()
# print(li2)
