"""
The 'happy' algorithm is:
• write down any integer
• square its digits and find the sum of the squares
• continue with this number
• repeat until either the answer is 1 (in which case the number is 'happy') 
  or until you get trapped in a cycle (in which case the number is 'unhappy')
"""

def sum_of_square_of_digits(number):
    total = 0
    
    for i in range(len(str(number))):
        total += int(str(number)[i]) ** 2

    return total

def is_happy(number):
    sums_of_squares_list = []
    square_sum = number
    while True:
        square_sum = sum_of_square_of_digits(square_sum)

        if square_sum == 1:
            print(f"Your number {number} is happy.")
            return True
        
        if square_sum in sums_of_squares_list:
            print(f"Your number {number} is unhappy.")
            return False
             
        sums_of_squares_list.append(square_sum)

if __name__ == "__main__":
    assert not is_happy(4)
    assert is_happy(70)
    assert not is_happy(110)

