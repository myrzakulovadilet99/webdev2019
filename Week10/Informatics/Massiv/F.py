n = int(input())
k = n-1
m = input().split()
for i in range(n):
	if k>=0:
		print(m[k])
	k-=1