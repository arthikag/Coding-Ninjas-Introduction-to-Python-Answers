from sys import stdin 
def swapElements(arr, start, end) :
    arr[start], arr[end] = arr[end], arr[start] 
    
def reverse(arr, start, end): 
    while(start < end):
        swapElements(arr, start, end)
        start += 1
        end -= 1 
def rotate(arr, n, d): 
    if n == 0 :
        return
    if d >= n and n != 0 :
        d = d % n
    reverse(arr, 0, n - 1) 
    reverse(arr, 0, n - d - 1) 
    reverse(arr, n - d, n - 1) 
def takeInput() :
    n = int(input())
    if n == 0:
        return list(), 0 
    arr = list(map(int, input().rstrip().split(" ")))
    return arr, n 
def printList(arr, n) :
    for i in range(n) : 
        print(arr[i], end = " ")
    print()

t = int(input())
while t > 0 :
    arr, n = takeInput()
    d = int(input()) 
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1