'''
The zip() function is used to combine two or more iterables, such as lists and tuples. 

e.g. zip(iterable1, iterable2, iterable3 ....) iterable1.len() == iterable2.len() and so on

combinations = (1,0,1,1)
variables = ["A", "B", "C", "D"]
frequency = (3,4,1,4)



'''

combinations = (1,0,1,1)
variables = ["A", "B", "C", "D"]
frequency = (3,4,1,4)

combined = zip(variables,combinations, frequency)


print(list(combined))
