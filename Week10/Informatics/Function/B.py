def my_fanc(a, b):
    k=1
    for i in range(b):
        k*=a
    return k

m = input().split()
a = int(m[0])
b = int(m[1])

print(my_fanc(a,b))
