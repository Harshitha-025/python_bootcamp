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
