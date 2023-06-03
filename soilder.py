from abc import abstractmethod
class soilder:
    @abstractmethod
    def who_re_u(self):
        pass

class healer(soilder):
    def who_re_u(self):
        print("I am healer")
        

class archer(soilder):
    def who_re_u(self):
        print("I am archer")
        
xsoilder=archer()
print(xsoilder.who_re_u)
zsoilder=healer()
print(zsoilder.who_re_u)