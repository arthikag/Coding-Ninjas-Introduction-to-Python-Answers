n=int(input())
print(1)
i=1
while(i<n):
    j=0
    while(j<i+1):
        if(j==0 or j==i):
            print(1,end="")
        else:
            print(2,end="")
        j=j+1
    i=i+1
    print()