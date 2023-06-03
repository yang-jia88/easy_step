#list funtion
word=["2","3","4","5","6"]
sentence="".join(word)
print(sentence)



#dict 使用方式
s1=(1,2,3,5,6,8)
print(s1[4])
s2_dict={"a":5,"b":6}
print(s2_dict["a"])


#(start,end,step)
for i in range(k-1,-1,-1):
    print(i)

#二維陣列 寫法
arr=[[0]*2 for i in range(2)]
print(arr)
arr[0][0]=int(input("a1="))
arr[0][1]=int(input("a1="))
arr[1][0]=int(input("a1="))
arr[1][1]=int(input("a1="))
print(arr)