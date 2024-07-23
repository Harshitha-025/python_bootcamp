#find the element that is present in k+n index 
k=int(input())
n=int(input())
list=list(map(int,input().split(" ")))
if(len(list)<k+n): 
    print("ERROR")
else:
    for i in range(1,len(list)):
        print(list[k+n])
        break
                  
#print the element in particular index
n=int(input())
list=list(map(int,input().split(" ")))  
print(list[n%len(list)])                  