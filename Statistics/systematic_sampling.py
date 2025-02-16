import random
import math

alphabet = [chr(i) for i in range(65, 91)]

N = len(alphabet) -1

n = 5

k = (N // n)

start = random.randint(1, k-1)

print(start)

sample = []

for i in range(start, N, k):
    sample.append(alphabet[i])

print(sample)
     