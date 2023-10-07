num=int(input("enter the number"))
num1=num
c=0
while(num>0):
    n=num%10
    c=c*10+n
    num=num//10
    print("c is",c)

print(c)    
if c==num1:
    print("number is palindrome")    
else:
    print("number is not palindrome")     