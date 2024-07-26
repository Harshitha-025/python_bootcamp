#write a program to find area of a circle 
#write a program to find perimeter of a circle
r=int(input())
pi=3.14
Area=pi*r*r
print("Area of circle=",Area)
perimeter=2*pi*r
print("perimeter of cirlce=",perimeter)

#write a program to find area of triangle
#write a program to find perimeterof a triangle
b=int(input())
h=int(input())
area=1/2*b*h
print("area of triangle=" ,area)
a=int(input())
c=int(input())
perimeter=a+b+c
print("perimeter of triangle",perimeter)

#find even or odd
num = int(input())
if (num % 2) == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd") 

#find greatest of three
num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is", largest)

#write a program to print first n fibonacci number series
a = int(input())
b = int(input())
n = int(input())
print(a, b, end=" ")
while n > 2:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    n -= 1