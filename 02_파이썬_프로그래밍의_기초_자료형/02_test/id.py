# a = [1, 2, 3]
# b = a

# id(a)
# print(id(a))
# print(id(b))

from copy import copy
a = [1, 2, 3]
b = copy(a)

print(id(a))
print(id(b))

c, d = ('python', 'life')

print(c)
type(c)
print(type(c))