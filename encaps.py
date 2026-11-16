class person:
    def __init__(self,name):      #parent constructor
        self.name=name
        pass


class student(person):
    def __init__(self,name,age):  #child constructor
        super().__init__(name)
        self.age=age
    def show(self):
        print(self.name,self.age)   


s1=student("Anu",20)

s1.show()