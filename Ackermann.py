#import math


def ackermann(a, b):
    if a == 0 and b >= 0:
        print((a, b))
        return b + 1
    elif b == 0 and a >= 0:
        print((a, b))
        return ackermann(a-1, 1)
    else:
        print((a, b))
        return ackermann(a-1, ackermann(a, b-1))


print(ackermann(3, 4))
