class A:
    def showA(self):
        print("class A")
class B:
    def showB(self):
        print("class B")
class C(A,B):
    pass
obj = C()
obj.showA()
obj.showB()                