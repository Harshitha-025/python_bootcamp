#password verifier-mrx is trying to create a new password for his instagram account.
# this are the required conditions for creating a new passsword
#condition1-min length is 8 and max length is 15
#condition2-only @,/ is allowed in a password
#condition3-no space are allowed
#condition4-only alpha numericsare allowed
#you are supposed to print weak-if length is exact 8
#medium-length is between 8 to12
#strong-if length is between 12 to 15
sp=["@","/"]
c=0
s=input()
n=len(s)
if ((n>=8 and n<=15) and (sp[0] in s or sp[1] in s) and (" " not in s)):
        if n==8:
            print("weak")
        elif n>=8 and n<=12:
            print("medium")
        elif n>=12 and n<=15:
            print("strong")
else:
    print("follow instructions")