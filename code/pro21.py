import statistics as st
counter=int(input(" "))
arr=list(map(int,input().split()))
result=False
for i in range(1,counter):
    l1=arr[:i]
    l2=arr[i:]
    if st.mean(l1)==st.mean(l2):
        result=True
if result==True:
    print("yes")
else:
    print("no")
