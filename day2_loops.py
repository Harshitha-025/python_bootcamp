mylist=list(map(int,input().split(" ")))
for i in range(len(mylist)):
    print(mylist[i],end=" ")#same line
    #print(mylist)#different lines
print()
s="hello" 
for i in range (len(s)):
    print(s[i])

#new problem
mylist=list(map(int,input().split(" ")))
choice=int(input())
t=len(mylist)
if(choice==1):
    mylist.append(10)
    print(mylist)
elif(choice==2):
    mylist.pop()
    print(mylist)
elif(choice==3):
    mylist.sort()
    print(mylist)
else:
    print(f"hello {t}")
