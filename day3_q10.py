#find the max element in a given list
list=list(map(int,input().split(" ")))
max=list[0]
for i in range(len(list)):
   if(list[i]>max):
    max=list[i]
print(max)

#find the min element in a given list
list=list(map(int,input().split(" ")))
min=list[0]
for i in range(len(list)):
   if(list[i]<min):
    min=list[i]
print(min)

#replace the elements in a array with average of max and min elements
list=list(map(int,input().split(" ")))
max=list[0]
min=list[0]
n=len(list)
newlist=[]
for i in range(len(list)):
   if(list[i]>max):
    max=list[i]
for i in range(len(list)):
   if(list[i]<min):
    min=list[i]
    sum=min+max
a=sum//2
for i in range(n):
  print(a,end=" ")