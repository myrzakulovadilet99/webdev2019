a = int(input())

i = 1
k = 0
while i<=a:
	if i==a:
		print("YES")
		k=1
		break
	i*=2
if k==0:
	print("NO")