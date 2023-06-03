
def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        l=list[:mid]
        r=list[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0

        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                list[k]=l[i]
                i+=1
            else:
                list[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            list[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            list[k]=r[j]
            j+=1
            k+=1


s1=[5,6,8,9,2,16,35,1,10]
mergesort(s1)
print(s1)

