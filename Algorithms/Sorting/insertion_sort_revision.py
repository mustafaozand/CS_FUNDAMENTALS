def insertion_sort(array):

    sorted = False

    i = 1
    j = i - 1

    while not sorted:
        j = i - 1

        if array[j] > array[i]:
            temp = array[i] 

            while array[j] > temp and j >= 0:
                array[j+1] = array[j]
                j -= 1

            array[j + 1] = temp

        i += 1

        if i >= len(array):
            sorted = True


  


