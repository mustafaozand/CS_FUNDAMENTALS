# Raspberry Pi Foundation
# Developed as part of Ada Computer Science
# 
# Usage licensed under CC BY-NC-SA 4.0


def quick_sort(items, start, end):
    """"A recursive quick sort algorithm"""
    
    # Base case for recursion:
    # The recursion will stop when the partition contains a single item
    if start >= end:
        return

    # Otherwise recursively call the function
    else:
        pivot_value = items[start] # Set to first item in the partition
        i = start + 1 # Set to second position in the partition
        j = end # Set to last position in the partition
        finished = False
        
        print(f"{items} Pivot value: {pivot_value}  Low mark: {i}  High mark: {j}")
        
        # Repeat until low and high values have been swapped as needed
        while finished == False:
            
            # Move the left pivot
            while i <= j and items[i] <= pivot_value:
                i = i + 1 # Increment low_mark
                
             # Move the right pivot                               
            while items[j] >= pivot_value and j >= i:
                j = j - 1 # Decrement high_mark

            # Check that the low mark doesn't overlap with the high mark
            if i < j:
                # Swap the values at low_mark and high_mark
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
                print(f"{items} Swapped the values {items[j]} and {items[i]}") # Testing
                
            # Otherwise end the loop
            else:
                finished = True
            
        # Swap the pivot value and the value at high_mark
        temp = items[start]
        items[start] = items[j]
        items[j] = temp
        print(f"{items} Swapped the pivot value {pivot_value} and {items[start]}\n") # Testing

   
        # Recursive call on the left partition
        quick_sort(items, start, j - 1)

        # Recursive call on the right partition
        quick_sort(items, j + 1, end)
    return items


def main():
    """Perform a quick sort on the test data"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    # test_items = [43,21,2,50,3,80,35,7,64] # Random
    test_items = [8,2,5,3,9,4,7,6,1]
    
    print("### Quick sort (recursive) ###")
    print(f"\nOriginal items {test_items} \n")

    # Assign the returned sorted array
    sorted_items = quick_sort(test_items, 0, len(test_items)-1)

    print(f"Sorted items {sorted_items}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()