count=int(input(" "))
array=[]
sss=[]
for i in range(count):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        sss.append(num)
sss.sort()
for i in sss:
    print(i,end=' ')
    #a
