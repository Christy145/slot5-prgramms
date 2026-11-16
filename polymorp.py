class Animal:
    def sound(self):
        print("Animal sound")
class dog (Animal):
    def sound(self):
        print("dog sound")
class cat(Animal):
    def sound(self):
        print("cat sound")

dog=dog()
dog.sound() 

cat=cat()
cat.sound()