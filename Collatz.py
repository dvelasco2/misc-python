import math
import random

def collatz(n):
    print("Collatz conjecture, input = " + str(n))
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 == 1:
            n = 3*n + 1
        else:
            print("Something went wrong.")
        print(n)
    print(n)

n = random.randint(1, math.pow(10, 8))
collatz(n)
