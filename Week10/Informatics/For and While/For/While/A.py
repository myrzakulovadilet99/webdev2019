import math

a = int (input())

b = 1

while b <=a:
    c = int(math.sqrt(b))
    if c * c == b:
        print(b)
        b+=1