class Animal:
    def speak():
        return "animal is speaking"
#single inheritance
class Dog(Animal):
    def Bark():
        return "Bow"
obj1=Animal
print(obj1.speak())
obj2=Dog
print(obj2.speak())
print(obj2.Bark())
#multilevel inheritance
class Puppy(Dog):
    def puppy_speak():
        return "im talking"
obj3=Puppy
print(obj3.speak())
print(obj3.Bark())
print(obj3.puppy_speak())
#multiple inheritance
class Father:
    def father_speak():
        return "Father speak"
class Mother:
    def mother_speak():
        return "Mother speak"
class kid(Mother,Father):
    def kid_speak():
        return "iam kid.im having properities"
obj1=kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())