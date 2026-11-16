class Father:
    def skills(self):
        print("driving")
class Mother:
    def skills(self):
        print("cooking")
class Child(Father,Mother):
    pass
obj=Child()
obj.skills()                