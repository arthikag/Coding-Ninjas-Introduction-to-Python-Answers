def printTable(start,end,step):
    curr_temp = start

    while curr_temp <= end:
        c = 5/9 * (curr_temp-32)
        print(curr_temp, " ", int(c))
        curr_temp = curr_temp+step
pass 
   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)