lines= int(input())
i=1 
while(i<=lines):# this loop is used to print lines  
    j=lines  
    while (j>=1):# this loop is used to print numbers in a line  
        if j!=i:  
            print(j, end='', flush=True)  
        else:  
            print('*', end='', flush=True)  
        j=j-1  
    print("")  
    i=i+1;  