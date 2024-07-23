#find the duplicates in an array
lists=list(map(int,input().split(",")))
li=[]
for i in lists:
     if(i not in li):
          li.append(i)
print(*li)

#sum of digits
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)

