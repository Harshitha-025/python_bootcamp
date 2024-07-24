#print the unique characters in a string
s=input()
n=s.lower()
ans=""
for i in n:
    if i not in ans:
        ans+=i
print(ans)

#input=hello123,output=6
check="0123456789"
s=input()
c=0
for i in s:
    if i in check:
       c+=int(i)
print(c)

#input=hello123world ,output=hello321world
check="0123456789"
s="hello123word"
ans=""
for i in s:
    if i in check:
        ans=i+ans
print("hello",ans,"world")