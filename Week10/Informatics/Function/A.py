def my_fanction(a, b):
    if a>b:
        return a
    else:
        return b

a = int (input())
b = int (input())
c = int (input())
d = int (input())

print(my_fanction(my_fanction(a,b), my_fanction(c,d)))

