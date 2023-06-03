s1=[1,2,3,4]
s2=[1,2,3,4]
print(s1 and s2) # 交集
print(s1 is s2) #不是copy會是false


x = ["apple", "banana", "cherry"]
y = x
print(x is y) #是copy會是true


x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)

