Number=int(input())
even=0
odd=0
while(Number>0):
    Reminder = Number %10
    if(Reminder % 2 == 0):
        even=even + Reminder
    else:
        odd= odd + Reminder
    Number = Number //10
print(even,"",odd)