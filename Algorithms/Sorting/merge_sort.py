
'''
Merge Sort
------------
O(n* log(n)) running time

1. Split array in half
2. Call Merge Sort on each half to sort them recursively
3. Merge both sorted halves into one sorted array
'''

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) //2] #Returns a slice 
        right_arr = arr[len(arr)//2:]

        # Recursion - the array will be divided until, a single element remains.

        merge_sort(left_arr) 
        merge_sort(right_arr)

        # Merge

        i = 0 # left arr index
        j = 0 # right arr index
        k = 0 # merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1

            else:
                arr[k] = right_arr[j]
                j += 1

            
            k += 1

        # If there are no more elements left to compare with then the leftover elements are added into the array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1






array_of_nums = [2,3,5,1,7,4,2,6,0]
merge_sort(array_of_nums)
print(array_of_nums)

