str1="14"
str2="433"
str3=str1.split()
str4=str2.split()
a=len(str3)
d=len(str4)
c=0
e=0
for i in range(a):
    b=int(str3[i])
    c=c*10+b
for j in range(d):
    f=int(str4[j])
    e=e*10+f
h=str(e+c)
g=str(h)
print(type(g),g)


