# input-->ABC,4
#op:- EFG
inp=input()
count=0
for i in inp:
     print(chr(ord(i)+4),end=" ")

# hello-----wor----ld
#op:---------helloworld
inp=input()
count=0
r=""
for i in inp:
    if i=='-':
        count+=1
    else:
      r=r+i
print("-"*count+r)
