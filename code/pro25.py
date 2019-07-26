#a
def LIS(arr,size):
    result=[]
    counter=1
    for i in range(0,size-1):
        if arr[i]<arr[i+1]:
            counter+=1
        else:
            result.append(counter)
            counter=1
    result.append(counter)
    print(max(result))
size=int(input())
arr=list(map(int,input(" ").split(" ")))
LIS(arr,size)
    
