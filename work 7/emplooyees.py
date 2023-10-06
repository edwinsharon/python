choice='y'
bank=[]
new_customer={}
acc_no=0
while choice=='y'or choice=='Y':
    print("""
1)add customer
2)display customer details
3)balance change
4)quit                                        

""")
    option=int(input("enter your choice:"))
    if option==1:
        name=input("enter the name of the customer:")
        new_customer["name"]=name
        age=int(input("enter the age"))    
        new_customer["age"]=age
        contact_number=int(input("enter the phone number"))
        new_customer["conatct"]=contact_number
        new_customer["acc_no"]=acc_no + 1
        new_customer["balance"]=0
        print(new_customer)
        bank.append(new_customer.copy()) 
    elif option==2:
        print(bank)
    elif option==3:
                    print("""
1)deposit
2)withdraw
enter your choice                          
                                    

""")
                    
           if