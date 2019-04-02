def my_fanc(a, b):
    if a!=b:
        return 1
    else:
        return 0

m = input().split()
a = int(m[0])
b = int(m[1])

print(my_fanc(a,b))