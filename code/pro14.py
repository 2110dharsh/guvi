#a
sbhava,imaha=map(int,input(" ").split(" "))
list2=list(map(int,input().split()))
sbhava=[]
list2.insert(0,0)
for y in range(imaha):
     vin=[]
     s=0
     bb,zz=map(int,input().split())
     for i in range(bb,zz+1):         
         s^=list2[i]     
     sbhava.append(s)
for y in sbhava:
     print(y)
