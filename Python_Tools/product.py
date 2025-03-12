'''
The product() function is part of Python's itertools module. 
It computes the Cartesian product of input iterables, which means it generates all posible combinations of elements from
the given iterables.

How it works?

It can take one or more iterables (list, tuples, strings) as arguents, and produces tuples containing
all combinations of elements from the input iterables.

You can specify how many times the iterables should be repeated by using the repeat parameter

'''

import itertools

list1 = [1,2,3]
list2 = ['a','b','c','d']
list3 = ['$','@']

result = list(itertools.product(list1,list2, list3))

print(result)