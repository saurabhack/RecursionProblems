def inversionCount(arr,n,counter):
    if n==0:
        return n
    i=inversionCount(arr,n-1,counter)
    for j in range(i+1,len(arr)-1):
        if arr[i]>arr[j]:
            counter+=1
    return counter
arr=[4,2,1,3,5]
n=len(arr)
print(inversionCount(arr,n-1,0))