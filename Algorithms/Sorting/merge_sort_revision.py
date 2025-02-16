def merge_sort(array):


    if len(array) > 1:

        left_array = array[:len(array) //2]

        right_array = array[len(array)// 2:]

        merge_sort(left_array)
        merge_sort(right_array)

        left_pointer = 0
        right_pointer = 0
        merge_pointer = 0

        while left_pointer < len(left_array) and right_pointer < len(right_array):
            if left_array[left_pointer] > right_array[right_pointer]:
                array[merge_pointer] = right_array[right_pointer]
                right_pointer += 1

            else:
                array[merge_pointer] = left_array[left_pointer]
                left_pointer += 1
            
            merge_pointer += 1

        while left_pointer < len(left_array):
            array[merge_pointer] = left_array[left_pointer]
            left_pointer += 1
            merge_pointer += 1

        while right_pointer < len(right_array):
            array[merge_pointer] = right_array[right_pointer]
            right_pointer += 1
            merge_pointer += 1



array = [3,1,10,5]

merge_sort(array)

print(array)