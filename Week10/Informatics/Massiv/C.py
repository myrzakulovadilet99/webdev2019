n = int(input())
s = input().split()
k = 0
for i in range(n):
	if int(s[i])>0:
		k+=1
print(k)