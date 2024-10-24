n=int(input())
count_root=0
while count_root**3<n:
    count_root+=1
if count_root**3==n:
    print("perfect cube")
else:
    print("not a perfect cube")
    