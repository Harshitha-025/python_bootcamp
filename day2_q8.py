#your given with a space seperated integer list,find no of even elements &odd elements in a given list
mylist=list(map(int,input().split(" ")))
odd=0
even=0
for i in range(len(mylist)):
  if(mylist[i]%2==0):
   even+=1
  else:
   odd+=1
print(even , odd)

#given an space seperated integer find an average of elements in a given index present in the even index
mylist=list(map(int,input().split(" ")))
sum=0
count=0
for i in range(len(mylist)):
    if(i%2==0):
      sum+=mylist[i]
      count+=1
print(sum/count)    