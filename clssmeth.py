class Student:
    def set_data(self,name,age):
        self.name = name
        self.age = age
    def show_data(self):
        print("Name:",self.name)
        print("Age:",self.age)    

obj = Student()
obj.set_data("Abin",20)
obj.show_data()
