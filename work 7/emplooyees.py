choice='y'
bank=[]
new_customer={}

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
        account=int(input("enter the account no. :"))
        new_customer["acc_no"]=account
        new_customer["balance"]=0
        print(new_customer)