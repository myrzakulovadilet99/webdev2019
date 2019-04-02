n = int(input())

s = input().split()

k = 0

for i in range(n):
    if (int(s[i-1])>=0 and int(s[i])>=0) or (int(s[i-1])<0 and int(s[i])<0):
        k+=1

if k == 0:
    print("NO")
else:
    print("YES")