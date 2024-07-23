#checking prime or not
n=int(input())
count=0
for i in range(2,int(n**0.5+1)):
    if n%i==0: 
        count=1
        break
if count==0:    
    print("prime")
else:
    print("not prime")

#write a program to print all the prime no in a given range
n=int(input())
m=int(input())
for i in range(n,m+1):
    for j in range(2,i):
      if i%j==0:
        break
    else:
        print(i)