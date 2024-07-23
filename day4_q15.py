#swapping 2no's
a=10
b=20
print(a+10,b-10)

#sum of n nos
n=int(input())
for i in range(n):
    res=(n*(n+1)//2)
print(res)

#to find lcm and gcd
a,b=map(int,input().split())
c,d=a,b
while(b!=0):
    a,b=b,a%b
print("gcd is ",a)
print("lcm is ",(c*d)//a)


