#a
bha=input(" ")
ya=map(int,input().split())
sin=[]
for i in ya:
    eat=bin(i)
    sin.append(eat)
fine=sorted(sin)
fine.reverse()
for j in fine:
    print(int(j,2))
