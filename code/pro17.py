#a
    
from itertools import permutations
n1, k1 = map(int, input(" ").split(" "))
x1 = list(map(int, input().split()))
for i in permutations(x1, 2):
    if sum(i) == k1:
        print('yes')
        break
else:
    print('no')
