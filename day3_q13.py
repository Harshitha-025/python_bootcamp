#find the sum of squares of a digit in a given  no
n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)

#sum of even digits
n=int(input())
sum=0
while n>0:
    r=n%10
    if(n%2==0):
       sum=sum+r
    n=n//10
print(sum)

#how to print reverse of a number
n=123
rev=" "
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))