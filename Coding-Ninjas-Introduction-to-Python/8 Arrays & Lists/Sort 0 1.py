from sys import stdin 
def sortZeroesAndOne(arr, n) : 
    nextZero = 0 
    for i in range(n) : 
        if arr[i] == 0 :
            temp = arr[nextZero] 
            arr[nextZero] = arr[i]
            arr[i] = temp 
            nextZero += 1 
def takeInput() :
    n = int(input().strip())
    if n == 0 : 
        return list(), 0 
    arr = list(map(int, input().strip().split(" "))) 
    return arr, n
def printList(arr, n) :
    for i in range(n) : 
        print(arr[i], end = ' ') 
    print()
t = int(input()) 
while t > 0 :
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n) 
    print() 
    
    t -= 1