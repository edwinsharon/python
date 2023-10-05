choice='y'
l1=[]
while choice=='y' or choice=='Y':
    print('''
1) add
2) delete
3) update
4) display
                              
          ''')
    a=int(input("enter your choice?"))
    if a==1:
        b=input("enter the task you want to schedule.")
        l1.append(b)
    elif a==2:
        b=input("enter the task u want to delete.")
        l1.remove(b)
    elif a==3:
        b=input("enter the priority u want to update")
        c=input("enter the new task you want to insert")
        l1[b]=c 
    elif a==4 :
        print("******TO DO LIST******")

        for i in l1:

            print("******",i,"******")  
    else:
        print("wrong choice")                

    option=input("do you want to continue (press y to continue)")
     
   