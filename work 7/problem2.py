num=[1,4,1,8,6,1]
val=1
for i in num:
    if i==val:
        del num[i]
print(len(num))
