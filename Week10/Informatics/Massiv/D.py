n = int(input())
s = []
s = input().split()

k = 0
c = 0

for i in range(1, n):
    if(s[i]>s[i-1]):
        k+=1
print(k)


