n = int(input())
arr = [int(ele) for ele in input().split()]
curr_max = arr[n-1]
ans = [arr[n-1]]
for i in range(n-2,-1,-1):
	if arr[i] >= curr_max:
		ans.append(arr[i])
		curr_max = arr[i]
for i in range(len(ans)-1,-1,-1):
	print(ans[i],end= ' ')