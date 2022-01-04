n=int(input())
n1=(n//2)+1
for i in range(1,n1+1):
    for j in range(1,n1-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
n2=n-n1
for i in range(n2,0,-1):
    for j in range(1,n1-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()