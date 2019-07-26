#a
n1, m1 = [int(i) for i in input(" ").split(" ")]
u1 = []
List = [int(i) for i in input().split()]
for _ in range(m1):
    l, k = [int(i) for i in input().split()]
    u1.append(min(List[l-1:k]))
for i in u1:
    print(i)
