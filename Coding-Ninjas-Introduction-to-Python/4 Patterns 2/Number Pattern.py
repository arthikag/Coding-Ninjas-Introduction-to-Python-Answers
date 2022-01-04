a=int(input())

for k in range(1,a+1):
    b='1'
    for i in range(2,a+1):
        c=str(i)
        if k >= i:
            b=b+c
        else:
            b=b+' '
    for j in range(a,0,-1):
        d=str(j)
        if k >= j:
            b=b+d
        else:
            b=b+' '
    print(b)