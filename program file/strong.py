def strongnumber(n):
    temp=n
    sum=0
    while temp>0:
        fact=1
        digits=temp%0
        for i in range(1,digit +1):
            fact=fact *i
        sum
        temp//=10
        if sum==n:
            print("strong number")
        else:
            print("Not a strong number")
n=int(input())
print(strongnumber(n))