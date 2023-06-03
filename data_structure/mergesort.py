i=j=k=0

list=[]
while i<m and j<n:
    if nums1[i]>nums2[j]:
                list[k]=nums2[j]
                j+=1
    else:
                list[k]=nums1[i]
                i+=1
            k+=1
    while i<m:
            list[k]=nums1[i]
            k+=1
            i+=1
    while j<n:
            list[k]=nums1[j]
            k+=1
            j+=1
print(list)

mylist=[1,1,2,3,5,8]
def plus1(a):
    list=[]
    n=0
    while n<len(mylist):
        b=mylist[n]+1
        list.append(b)
        n+=1
    return list

print(plus1(mylist))
