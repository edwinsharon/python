# num=int(input("enter a number"))
# c=0
# while(num>0):
#     n=num%10
#     c=c*10+n
#     num=num//10
# print(c)    

num=input("enter a number")
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0

for p in range(len(num)):
    if num[p]=='1':
        a+=1
    elif num[p]=='2':
        b+=1
    elif num[p]=='3':
        c+=1
    elif num[p]=='4':
        d+=1   
    elif num[p]=='5':
        e+=1
    elif num[p]=='6':
        f+=1
    elif num[p]=='7':
        g+=1
    elif num[p]=='8':
        h+=1
    elif num[p]=='9':
        i+=1
    elif num[p]=='0':
        j+=1                                 
for k in range(a-j):
    print(a)

