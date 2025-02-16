'''
Quick Sort 
-----------

A divide and conquer algorithm, simply because it reduces the size of the problem into smaller subproblems that are more easily solvable.

Now, one of the reasons why quick sort operates faster than merge sort is because, it does not rely on any additional memory space as it operates.

Step-by-step Explanation
--------------------------

'''

def quick_sort(array, start, end):

    if start < end:

        pivot = partition(array, start, end)

        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, end)


def partition(array, start, end):
    
    pivot = array[end]

    i = start - 1


    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]

        
        # This is where we pick our new pivot position

    array[i + 1], array[end] = array[end] , array[i + 1]

    return i + 1 # Our pivot's new position will be i + 1


array = [10,7,9,8,1,5]

quick_sort(array=array, start=0, end=(len(array)-1))

print(array)

            
