# my_list=[1,2.3,'sad',True,[1,4,7]]

# numbers=[1,2,3,4,5,6,7]
# sub_list=numbers[1:5]
# print(sub_list)

# list1=[1,2,3]
# list2=[4,5,6]
# combined_list=[list1+list2]
# print(combined_list)

# fruits=['apple','banana','cherry']
# fruits.append('kiwi')
# print(fruits)
# fruits.insert(1,"orange")
# print(fruits)
# fruits.append('grape')
# fruits.append('blueberry')
# print(fruits)
# fruits.remove("banana")
# print(fruits)


# numbers=[5,2,8,1,3]
# numbers.sort()
# a=numbers
# print(a)
# numbers.sort(reverse=True)
# b=numbers
# print(b)


# my_list=[1,2.3,'sad',True,[1,4,7]]
# print(my_list[-1])


# fruits=['apple','banana','cherry']
# fruits.append('kiwi')
# print(fruits)
# fruits.insert(1,"orange")
# print(fruits)
# fruits.append('grape')
# fruits.append('blueberry')
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# x = fruits.count("apple")
# print(x)

# num=[5,2,8,1,3]
# a=num[::-1]
# print(a)

# original_list=[1,2,3]
# copied_list=original_list.copy()
# print(copied_list)
# copied_list.append(4)
# print(copied_list)
# print(original_list)




# numbers = [5,2,8,1,3] 
# result = map(, numbers) 
# print(list(result)) 


# numbers = [5,2,8,1,3] 
# print(max(numbers))
# print(min(numbers))

# fruits=['apple','banana','cherry']
# print('banana' in fruits)


# fruits=['apple','banana','cherry']
# print(len(fruits))


# fruits=['apple','banana','cherry']
# fruits.remove("banana")
# fruits.insert(1,'grapefruit')
# print(fruits)


# a=int(input("enter the bill amount"))
# if a>100:
#     c=a/10
#     b=a-c
#     print("the discounted bill is:" ,b)
# elif a>50 and a<100:
#     c=a/20
#     b=a-c
#     print("the discounted amount is:",b)   
# else:
#     print("no discount")    



# a=int(input("enter the year"))
# if a%4==0:
#     print(a,"is a leap year")
# else:
#     print("it is not a leap year.")

# a=(int(input("""enter your choice
#              1. celcius to farenheit
#              2. farenheit to celcius""")))
# b=(int(input("enter the temperatre")))
# if a==1:
#     c=a*9
#     c=c/5
#     c=c+32
#     print(c,'farenheit')
# elif a==2:
#     c=a-32
#     c=c*5
#     c=c/9
#     print(c,"celcius")
# else:
#     print("wrong choice")    



secret=25
g=int(input("enter a number between1-100"))
if g>25:
    print("to high")
elif g<25:
    print("to low")  
else:
    print("correct")      