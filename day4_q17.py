#leap year or not
n=int(input())
if(n%4==0 and n/100!=0):
    print("leap year")
else:
    print("not leap year")

#leap year or not in range
m=int(input())
n=int(input())
for i in range(m,n+1):
      if(i%4==0 and i/100!=0):
         print(i)

