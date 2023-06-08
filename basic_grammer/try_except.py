a = 0
b = "1"
try :
    print(a)
    print(b+1)
except NameError:
    print("none difine")
except TypeError:
    print("type error")
print("00")