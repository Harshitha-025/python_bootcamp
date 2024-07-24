#intialising class
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return(a*b)
    def div(a,b):
        return(a//b)
    def mod(a,b):
        return(a%b)      

obj1=Myclass
print(obj1.add(3,4)) 
print(obj1.sub(5,6))
print(obj1.mul(7,8)) 
print(obj1.div(9,2)) 
print(obj1.mod(1,3)) 

#constructor
class Myclass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b  
obj1=Myclass
print(obj1.add(3,4)) 

