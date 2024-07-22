#arithematic operator
a=int(input())
b=int(input())
print("addition od number",a+b)
print("subtraction od number",a-b)
print("multiplication od number",a*b)
print("division od number",a/b)
print("power of a and b",a**b)
print(a//b)#round fig value of division
print(a%b)#modulus of a and b

#logical operators-or,and
age=25
if(age>=18 and age<24):
  print("two wheeler")
elif(age>=24 and age<45):
  print("two and four wheeler")
else:
   print("all") 

t=700
a=int(input())
b=int(input())
o=int(input())
acost=13
bcost=4
ocost=5
tot=a*acost+b*bcost*12+o*ocost
if tot>t:
    print("cheated")
else :
    print("not cheated")

#given no postive or negative and odd or even
a=int(input())
if a<0 and a%2==0:
    print("no is negative and even")
elif a<0 and a%2!=0:
    print("no is negative and odd")
elif a>0 and a%2!=0:
    print("no is positive and odd")
else :
    print("no is positive and even")