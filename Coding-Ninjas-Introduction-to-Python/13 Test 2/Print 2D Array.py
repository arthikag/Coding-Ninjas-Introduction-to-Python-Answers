def print2DArray(mat, rows, cols) :
	k = rows
	for i in range(rows) :
		for l in range(k-1, -1, -1) :
			for j in range(cols) :
				print(mat[i][j], end = " ")
			print()
		k -= 1 #main
mat = []
li = input().strip().split()
rows = int(li[0])
cols = int(li[1])
for i in range(rows) :
	row = [int(elem) for elem in list(input().strip().split())]
	mat.append(row)
print2DArray(mat, rows, cols)