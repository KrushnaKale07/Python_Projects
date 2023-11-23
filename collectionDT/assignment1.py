# Q1: add 5 elements in a set

s1 = {1,2,3,4,5}
print('Original set1')
print(s1)
print()

# s1.add(6)
# s1.add(7.7)
# s1.add(True)
# s1.add('John')
# s1.add(False)

# print(s1)
# //{False, 1, 2, 3, 4, 5, 6, 7.7, 'John'}

# Q2: Remove randon element from set

# s1.pop()
# print(s1)
# //randiom output {2, 3, 4, 5}

# Q3: Remove specific element from set

# s1.remove(4)
# print('Removing specific element from set using remove method')
# print(s1)
# //randiom output{1, 2, 3, 5}

# s1.remove(7)
# print('Removing specific element from set using remove method')
# print(s1)
# //KeyError: 7

# s1.discard(2)
# print('Removing specific element from set using discard method')
# print(s1)
# //{1, 3, 4, 5}

# --------------------------------------------------------------------------------------------------------------------------------------------------

s2 = {3,8,9}
print('Original set2')
print(s2)
print()

# Q4: Check common element between two set

# print('Using intersection method')
# print(s2.intersection(s1))
# //{3}

# Q5: check differnt element from one set to another set

# print('Using differnce method')
# print(s1.difference(s2))
# //{1, 2, 4, 5}

# print('Using differnce method')
# print(s2.difference(s1))
# //{8, 9}

# Q6: Combine two sets

# print('Using union set')
# print(s1.union(s2))
# //{1, 2, 3, 4, 5, 8, 9}

# Q7: Copy combined set

# print('copied combined set')
# print((s1.union(s2)).copy())
# # //{1, 2, 3, 4, 5, 8, 9}

# Q8: clear all the set element4

# print('After clear all the set element')
# s1 = s1.clear()
# print(s1)

# s2 = s2.clear()
# print(s2)
