a=input("enter your password")
b=len(a)
c=a.split()
d,e,f,g,h=0,0,0,0,0
for i in range(b):
    if(a[i]==a.isalpha()):
        d=d+1
    elif(a[i]==a.isnumeric()):
        e=e+1
    elif(a[i]!=a.isalnum()):
        f=f+1
    elif(a[i]==a.islower()):
        g=g+1
        
    elif(a[i]==a.isupper()):
        h=h+1
if(d>0 and e>0 and f>0 and g>0 and h>0):
    print("your password is strong")                    
else:
    print("your password is weak")