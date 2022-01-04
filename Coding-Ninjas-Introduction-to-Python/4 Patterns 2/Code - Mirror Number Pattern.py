n=int(input())
for x in range(1,n+1):
    for y in range(n,x,-1):
        print(" ",end="")
    for z in range(1,x+1):
        print(z,end="")
    print("")