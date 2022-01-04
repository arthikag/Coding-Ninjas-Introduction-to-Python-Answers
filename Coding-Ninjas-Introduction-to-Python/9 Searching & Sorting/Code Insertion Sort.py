from sys import stdin 
def insertionSort(arr, n) :
    i = 1 
    while i < n :
        temp = arr[i]
        j = i - 1
        while j >= 0 :
            if arr[j] > temp :
                arr[j + 1] = arr[j] 
            else :
                break 
                
            j -= 1 
            
        arr[j + 1] = temp
        i += 1

def takeInput() : 
    n = int(input())
    if n == 0 : 
        return list(), 0 
    arr = list(map(int, input().strip().split(" "))) 
    return arr, n 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ") 
    print() 

t = int(input())
while t > 0 :
    arr, n = takeInput()
    insertionSort(arr, n)
    printList(arr, n) 
    t-= 1