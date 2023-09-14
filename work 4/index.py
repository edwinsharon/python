l=[10,20,30,4,"python"]
b=[0]
b[0]=l[0]
l[0]=l[4]
l[4]=b[0]
print(l)
l=[10,20,30,4,"python"]
c=l[0]+l[1]
print(c)
l=[10,20,30,4,"python"]
print(len(l))
l1=[3,6,7]
l+=l1
print(l)
l=[10,20,30,4,"python"]
l.insert(4,"g")
print(l)
l=[10,20,30,4,"python"]
def Reverse(l):
   new_lst = l[::-1]
   return new_lst
print(l)
l=[10,20,30,4,"python"]
l.clear()
print(l)
# del l
# print(l)