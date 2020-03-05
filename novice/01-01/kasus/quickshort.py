def quickshort(a,start,end):
    if start<end:
        pindex = partition(a,start,end)
        quickshort(a,start,pindex-1)
        quickshort(a,pindex+1,end)
 
def partition(a,start,end):
    middle = int(end/2)
    pivot = a[middle]
    pindex = start
    for i in range(start,middle):
        if a[i]>=pivot:
            a[i],a[pindex]=a[pindex],a[i]
            pindex = pindex + 1
    a[pindex],a[middle]=a[middle],a[pindex]
    print(a)
    return pindex
 
a = [68,90,78,44,34,20,100,56,34,2]
quickshort(a,0,len(a)-1)