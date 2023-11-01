import master
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("""
               1.addition
               2.subtraction
               3.multiplication
               4.division
            """))
if c==1:
    master.add(a,b)
elif c==2:
    master.diff(a,b) 
elif c==3:
    master.pro(a,b)    
elif c==4:
    master.quo(a,b)    


