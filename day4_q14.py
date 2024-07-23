#one peek value
n=list(map(int,input().split( )))
count=0
for i in range(1,len(n)-1):
   if n[i]>n[i-1] and n[i]>n[i+1]:
        count=1
        break
print(count)
print(n[count])

#all peek elements
n=list(map(int,input().split( )))
count=0
for i in range(1,len(n)-1):
   if n[i]>n[i-1] and n[i]>n[i+1]:
       count=i
        #print(n[i],end=" ")
if(n[-1]>n[-2] and n[1]>count):
 count=len(n)-1
print(n[count])