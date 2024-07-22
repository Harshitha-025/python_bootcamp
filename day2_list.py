#using list 
list=[1,2,3]
print(list)
print(*list)
list.append(55)#adds element at last
print(list)
list.insert(3,7)
print(list)
list.pop(2)#2 is index value
print(list)
list.insert(4,8)#index value,number to be inserted
print(list)
print(len(list))
newlist=list.copy()
print(newlist)
cnt=list.count(2)
print(cnt)
list.sort()
print(list)
