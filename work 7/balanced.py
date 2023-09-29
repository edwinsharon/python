a=input("enter the string")
c=0
for i in a:
    if i=='a':
        c+=1
    elif i=='b':
        c-=1
if c==0:
    print("string is balanced")
else:
    print("string is unbalanced")    