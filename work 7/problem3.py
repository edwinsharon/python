
def floorSqrt(x):
 
   
    if (x == 0 or x == 1):
        return x
 
    
    i = 1
    result = 1
    while (result <= x):
 
        i += 1
        result = i * i
 
    return i - 1
 
 

x=int(input("enter the number"))
print(floorSqrt(x))

#  list=["flower","flow","flight"]
# for h in len(list):
#    for i in list[h]:
#       for k in list[h+1]:
#          for j in list[h+2]:
#             if i==k==j:
#                print(i)

    
   
 
 
