dial={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
c=int(input("enter the number"))
f=c
k=0
l=0

while(f>0):
    n=f%10
    k=k*10+n
    f=f//10
    l+=1
if l==1:
    print(dial[c])
   
elif l==2:
     d=c//10
     c=c%10
     a=dial[d]
     b=dial[c]
     for i in a:
        for j in b:
           print(i+j,"")
     print("")
elif l==3:
    d=c%10
    p=c//10
    q=p%10
    g=p//10
    t=g%10
    a=dial[d]
    b=dial[q]
    w=dial[t]
    for s in a:
        for u in b:
            for z in w:
                print(s+u+z,"")




