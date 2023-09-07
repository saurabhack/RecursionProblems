def partition(arr,s,e):
    d=arr[s]
    counter=0
    for i in range(s+1,len(arr)):
        if arr[i]<d:
            counter=counter+1
    index=s+counter
    arr[index],arr[s]=arr[s],arr[index]
    i=0
    j=len(arr)-1
    while i<index and j>index:
        while arr[i]<=index:
            i+=1
        while arr[j]>index:
            j-=1
        if i<index and j > index:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return index
def QuickSort(arr,s,e):
    if s>=e:
        return
    p=partition(arr,s,e)
    QuickSort(arr,s,p)
    QuickSort(arr,p+1,e)
arr=[3, 2, 4, 1, 5]
QuickSort(arr,0,len(arr)-1)
print(arr)