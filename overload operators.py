class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
       if(self.a<other.a):
           return "Obj1 is less than Obj2"
       else:
           return "Obj2 is less than Obj1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "Both are equal"
        else:
            return "Not equal"
obj1=A(2)
obj2=A(3)
print(obj1<obj2)
print(obj1==obj2)