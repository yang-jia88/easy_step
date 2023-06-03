# sum=0
# n=1
# for n in range(10):
#     sum=sum+n
# print(sum)
def multiply(n1,n2=1):#如果後面不給值，則設1
    print(n1*n2)
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))



if __name__ == "__main__":
    multiply(5,6)
    multiply(5)
    multiply(4)
    avg(5,6,6,8,8,9,50)