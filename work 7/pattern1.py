
# a=(input("enter number with spaces"))
# a.split(' ')
# # b=[]
# # for i in range(len(a)):
# # #    b.append(int(a[i]))
# #     # print((a[i]))
# #     b.append(a[i])

# a.sort()

# # print(b[1],"second smallest")
# # print(b[-2],"second largest")

a=int(input("how many elements you want to insert"))
b=[]
for i in range(a):
    c=int(input("enter the element"))
    b.append(c)
print(b)
b.sort()
print(b[1],"second smallest")
print(b[-2],"second largest")