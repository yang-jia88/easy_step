def solution(s):
    lst=[]
    if len(s)%2==1:
        s=s+"_"#加入下底線
        print(lst)
    for x in range(0,len(s),2):#0到長度 然後x一次加2
        lst.append(s[x:x+2])#將x到x+1的位置放入lst陣列
    print(lst)
    return lst
while True:
    print(1)