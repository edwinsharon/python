# a=int(input('enter your number'))
# for i in [6,3,8,4,9,1,2,4]:
#     print(i*'*')
x=1
for i in range(1,6):
    for j in range(1,i):
       print(x,end=' ')
       x=x+1
    print('')