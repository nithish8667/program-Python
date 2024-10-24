def find_subarray_sum(n,prices,targetsum):
    startindex=0
    currentsum =0
    for endindex in range(n):
        currentsum += prices[endindex]
        while currentsum > targetsum and startindex <= endindex:
            currentsum -= prices[startindex]
            startindex += 1
        if currentsum == targetsum:
            return [startindex+1,endindex+1]
    return[-1]
n=5
prices=[1,2,3,4,5]
targetsum=9
print(find_subarray_sum(n,prices,targetsum))






n=5
lis=[1,2,3,4,5]
tar=10
val=0
for i in range(n):
    ele=lis[i]
    for j in range(i+1,n):
        ele+=lis[j]
        if ele==tar:
            print(i+1,j+1)
            break
        if ele==tar:
            break