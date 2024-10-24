li=list(map(int,input().split()))
p=[]
for i in li:
    for j in range(1,i):
        if i%j==0:
            p.append(j)
print(*p)