def EvenNums(num):
    assert num % 2 == 0, "Your number must be even, it can't be odd."

    print(num)

    if num == 2:
        return num
    
    else:
        return EvenNums(num - 2) # Here the number - 2, will be stored inside the memory, and then the
                                 # function will still be called, with num - 2, and this process will repeat until a base case has been reached.


def Fibonacci_Sequence(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return Fibonacci_Sequence(n - 2) + Fibonacci_Sequence(n - 1)
    
def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)

print(factorial(6))

print(Fibonacci_Sequence(5))