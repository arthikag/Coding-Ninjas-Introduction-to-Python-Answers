def checkArmstrong(n):
    digits = 0
    num = n
    while(num > 0):
        digits = digits + 1
        num = num//10
    newNum = 0
    num = n
    while(num > 0):
        last = num%10
        newNum = newNum + (last**digits)
        num = num // 10
    if(newNum == n):
        return True
    else:
        return False
n = int(input())
if(checkArmstrong(n)):
    print("true")
else:
    print("false")