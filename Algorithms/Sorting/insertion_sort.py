'''
Insertion Sort
--------------
Time Complexity: O(n^2)
Space Complexity: O(1)

Step-by-step:
-------------
1. Starts from the second element i = 1, because you assume that the first element is already sorted.
2. In each iteration arr[i] is the value that is to be inserted into the sorted subarray arr[0, i-1].
3. Start comparing key (arr[i]) with the elements in the sorted subarray arr[0, i-1].
4. This comparison is carried out from right to left
and if the key is smaller than the element, then the element is shifted to the right, and the key is inserted in its place.
5. This process is repeated until the key is greater than the element.

'''


def insertion_sort(arr):
    i = 1
    sorted = False
    
    while not sorted:
        j = i - 1

        if arr[i] < arr[j]:
            temp = arr[i]

            while arr[j] > temp and j >= 0:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j+1] = temp

        i += 1

        if i >= len(arr):
            sorted = True


arr = [3,5,26,2,62,35,32,52]

print(arr)

insertion_sort(arr)

print(arr)







        


                

            