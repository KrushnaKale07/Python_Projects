# SET

# we can store hetrogeneous datatype in set
# set is unorder in nature

# s1 = {10, 12.23, True, 'ram'}
# print('This is oringinal set')
# print(s1)
# print()

# add()
# it is use to add element in a set

# print('Using add method')
# s1.add(False)
# print(s1)
# // {10,False, 12.23, True, 'ram'}

# pop()
# it is use to delete random element in a set

# print('Using pop method')
# s1.pop()
# print(s1)

# remove()
# it is use to delete specific element from a set

# print('Using remove method')
# s1.remove(10)
# print(s1)
# //{True, 12.23, 'ram'}

# s1.remove(45)
# print(s1)
# //KeyError: 45

# discrd()
# it is use to overcome disadvantage of remove method of set
# it is use to delete specific element from the element

# print('Using discard method')
# s1.discard('bruh')
# print(s1)
# //{True, 10, 'ram', 12.23}

# s1.discard(10)
# print(s1)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# intersection method
# It is use to identify common element from two sets

s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {2,4,6,8}

# print('Using intersection method')
# print(s1.intersection(s2))
# //{8, 2, 4, 6}


# difference method
# it is use to identify the different element from the one set to another set

# print('Using difference method')
# print(s1.difference(s2)
# //{1, 3, 5, 7, 9, 10}

# union method
# it is use to combine two set

# print('Using union method')
# print(s1.union(s2))
# //{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# issubset method
# it is use to check whether a one set is subset of another set or not
# it gives output in bool format

# print('Using issubset method')
# print(s1.issubset(s2))
# //False

# print(s2.issubset(s1))
# //True

# clear()
# it is use to delete all the element from the set

# s1.clear()
# print(s1)
# //set{}

# s2.clear()
# print(s2)
# //set{}

# copy method
# it is use to copy a set

# s3 = s2.copy()
# print(s3)
# //{8, 2, 4, 6}
