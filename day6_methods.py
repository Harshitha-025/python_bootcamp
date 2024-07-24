#method over riding-compile time
class Animal:
    def Speak():
        return "Speaking...."
class Dog(Animal):
    def Speak():
        return "Dog is speaking..."
class puppy(Dog):
    def Speak():
        return "Puppy is speaking..."
obj1=puppy
print(obj1.Speak())

def run():
    return "running"
def run():
    return "hello"

#method overloading-runtime
class cal:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return sum
#take inputs:
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))




    

    