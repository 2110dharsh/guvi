k,m=map(int,input(" ").split(" "))
mk=list(map(int,input().split()))
l=[]
for i in range(0,m):
     a,b=map(int,input().split())
     l.append([a,b])
for i in range(m):
     lower=l[i][0]
     upper=l[i][1]
     x=sum(mk[lower-1:upper])
     print(x)
