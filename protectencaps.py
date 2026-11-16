class Student:
    def __init__(self,name):
        self._name=name
    def show(self):
        print(self._name)


s=Student("Anu")
print(s._name)            
