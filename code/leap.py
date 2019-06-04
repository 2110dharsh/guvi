year=int(input())
if(year%4==0 and year%100!=0 or year%400==0):
    print("yes")
elif(year%4!=0 and year%100==0 or year%400!=0):
    print("no")
else:
    print("invalid")
