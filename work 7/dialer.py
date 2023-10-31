dial={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
c=int(input("enter the number"))
h=list(dial[c])
print(h)
g=len(h)

if g==1:
    print(h)
   
    
elif g==2:
     d=c//10
     c=c%10
     a=dial[d]
     b=dial[c]
     for i in a:
        for j in b:
           print(i+j,"")
     print("")




