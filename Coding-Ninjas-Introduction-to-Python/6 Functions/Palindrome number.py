def checkPalindrome(num):
    numb=str(num)
    temp=numb
    if numb[::-1]==temp:
        return 1
    else:
        return 0
pass
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
    print('true')
else:
    print('false')