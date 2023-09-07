def sortingArray(arr,n):
    if n==0 or n==1:
        return
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    sortingArray(arr,n-1)
if __name__=="__main__":
    arr=list(map(int,input().split()))
    n=len(arr)
    sortingArray(arr,n)
    print(arr)