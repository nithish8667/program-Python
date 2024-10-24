import math
li=list(map(int,input().split()))
n=[]
print(li)
for i in li:
    if math.sqrt(i)==math.floor(math.sqrt(i)):
        n.append(i)
print(*n)
# with using inbuilt