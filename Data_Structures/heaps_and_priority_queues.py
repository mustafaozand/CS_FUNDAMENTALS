import heapq

# data = [10,20,43,1,2,65,17,44,2,3,1]
# new_data = []
# for i in data:
#     new_data.append(-i)

# data = new_data




# heapq.heapify(data)



# print(data)

# copy = data[:]

# print(heapq.heappop(data))
# print(copy.pop(0))

# print(data)

'''
i
first child is at 2i + 1
second child is at 2i + 2
parent is at (i -1)/ 2


'''

l1 = [10,20,30,40,50]
l2 = [15,25,35,45,55]

l3 = heapq.merge(l1, l2)

print(list(l3))