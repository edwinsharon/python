a=input("enter a string")
b=a
# b=
for i in a.split(' '):
    print(i[::-1])
    if i==i[::-1]:
       print(len(i)*'@')
       
        
        
           
    else:
        print('not')

print(b)

    

