#taking input
n=int(input())
print(n)
print("SRIDEVI WOMEN'S ENGINEERING COLLEGE")

#variable declaration
var1="python"
print("good morning",var1)

##fstring formatted string usedfor combination of characters and numbers
name=input("enter your name")
age=input("enter your age")
print("hello",name)
print(f"HELLO {name} you are {age} years")

#average of marks
name=input("enter your name")
m1=int(input())
m2=int(input())
m3=int(input())
print(f"HELLO {name} you are marks are{m1+m2+m3}and average is {(m1+m2+m3)/3} ")

#END IS USED TO GET DESIRED OUTPUT
#CONDITIONAL STMT-IF,ELIF,ELSE,
name=input()
age=int(input())
if age<=18:
  print(f"hello {name} you are {age} not eligible")
else: 
   print(f"hello {name} you are {age} eligible")
