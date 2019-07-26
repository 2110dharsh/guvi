#a
    
s=int(input(" "))
m=list(map(int,input().split()))
m.sort()
sin=0
s=0
for i in range(len(m)):
    if m[i]>=sin:
        s=s+1
    sin=sin+m[i]
print(s)
