#take a space separated and print alternate no in a list
mylist=list(map(int,input().split()))
for i in range(0,len(mylist),2):
    print(mylist[i])

#even no printing
mylist=list(map(int,input().split(",")))
for i in range(0,len(mylist),2):
    print(mylist[i])

#count 
list=list(map(int,input().split(",")))
count=0
for i in range(1,len(list),2):
    count+=1
print(count)