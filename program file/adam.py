n=int(input())
sq=n*n
b=int(str(n)[::-1])
sq1=b*b
sq=int(str(sq)[::-1])
if sq1==sq:
    print("Yes")
else:
    print("No")
    