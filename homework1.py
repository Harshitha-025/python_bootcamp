  #Find whther given no. Is palondrome Or not
num=int(input())
rem=0
res=0
temp=num
while(num>0):
    rem=num%10
    res=(res*10)+rem
    num=num//10
if res==temp:
    print("palindrome")
else:
    print("not a palindrome")

#Check whether given no. Is armstrong Or not
arm=int(input())
sum=0
copy_arm=arm
no_of_digits=len(str(arm))
while(arm>0):
    digit1=arm%10
    sum+=digit1**no_of_digits
    arm=arm//10
if sum==copy_arm:
    print(copy_arm,"is a armstrong")
else:
    print(copy_arm,"is not a armstrong")


#Check whether no. Is friendly or not
num1=int(input())
num2=int(input())
sum1=0
sum2=0
for i in range(1,num1):
   if(num1%i==0):
      sum1=sum1+i
for i in range(1,num2):
   if(num2%i==0):
      sum2=sum2+i
if num1/num2==sum1/sum2:
   print("It is a Friendly Pair")
else:
   print("It is not a Friendly Pair")

#Check whether no. Is strong or not
sum=0  
num=int(input())   
temp=num  
while(num):   
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("Given number is a strong number")  
else:  
    print("Given number is not a strong number")  

#Find sum of first 10 natural numbers
n=int(input())
for i in range(n):
    res=(n*(n+1)//2)
print(res)
