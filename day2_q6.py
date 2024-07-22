#printing n elements
n=int(input())
for i in range(1,n):
    print(i,end=" ")
    
#inserting elements
list=list(map(int,input().split()))
n=int(input())
for i in range(1,n+1):
    list.append(i)
print(*list)

#sum of elemts
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

