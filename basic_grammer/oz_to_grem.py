class oztogrem:
    def __init__(self,type):
        self.type = type
        if self.type==1:
            self.x=31  
        else:
            self.x=28
    def change(self,oz):
        print(oz*self.x)
        
item1=oztogrem(1)
item1.x=30
item1.change(10)


