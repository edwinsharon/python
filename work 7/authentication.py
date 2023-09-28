username=["edwin","sharon","shajan"]
password=["volleyball","cricket","football"]
a=input("enter your username")
b=input("enter your password")
authenticated=False
for i in range(len(username)):
    if a==username[i] and b==password[i]:
       authenticated=True
if authenticated:
    print("athentication confirmed")      
else :
    print("authentication failed")     