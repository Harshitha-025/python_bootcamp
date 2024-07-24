#check how many vowels are in a string
check=['a','e','i','o','u']
s=input()
inp=s.lower()
count=0
for i in inp:
    if i in check:
        count+=1
print(count)

#to print consonants
abc="bcdfghjklmnpqrstvwxyz"
s=input()
inp=s.lower()
for i in inp:
    if i in abc:
        print(i,end="");

#print all the vowels followed by consonants
abc="bcdfghjklmnpqrstvwxyz"
check=['a','e','i','o','u']
ans=""
s=input()
inp=s.lower()
for i in inp:
    if i in check:
        ans+=i
for i in inp:
    if(i in abc):
        ans+=i
print(ans)

