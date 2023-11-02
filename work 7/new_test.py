import pickle
L=[]
price=[]
Price=[2000]

def room_info():
    global price
    global L
    global Price
    a=open("Marine.dat","wb+")
    room=[]
    l2=[]
    print("1. Standard Non-AC - Rs. 3500")
    print("2. Standard AC - Rs. 4000")
    print("3. 3-Bed Non AC - Rs. 4500")
    print("4. 3-Bed AC - Rs. 5000")
    n=int(input("ENTER NUMBER OF ROOMS"))
    for i in range(n):
        ch=int(input("ENTER YOUR CHOICE"))
        if ch == 1:
            room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")
            price.append(3500)
            print("Price- 3500")
        elif ch == 2:
            room.append('Standard AC ')
            print("Room Type- Standard AC")
            price.append(4000)
            print("Price- 4000")
        elif ch == 3:
            room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            price.append(4500)
            print("Price- 4500")
        elif ch == 4:
            room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            price.append(5000)
            print("Price- 5000")
        else:

            print(" Wrong choice..!!")
    l2=[room,price]
    L.append(l2)
    Price.append(price)
    pickle.dump(L,a)
   
    print("")
    print("\t\t\t*ROOM BOOKED SUCCESSFULLY*\n")
    a.close()

def payment():
    global L
    ob=open("Marine.dat","wb+")
    a='y'
    while a=='y' or a=='Y':
        ph=str(input("Phone Number-"))
        co=str(input("ENTER CHECK-OUT DATE IN DD/MM/YYYY"))
        d=int(input("Enter your total days in Marine View"))
        print("---------PAYMENT----------")
        print("MODE OF PAYMENT")
        print("1-Credit/Debit Card")
        print("2-Using UPI")
        print("3-Cash")
        print("Your Total Bill Is")
        print(sum(Price))
        ch=int(input("Enter Your Mode Of Payment"))
        if ch==1:
            print("PAYING FOR MARINE VIEW")
            print("Pay In The Reception")
            print("THANKYOU")
            print("VISIT AGAIN :)")
        elif ch==2:
            print("PAYING FOR MARINE VIEW")
            print("UPI Number is: 974XXXXXXXX")
            print("If we recieved the payment we will notify you with a message")
            print("THAKYOU")
            print("VISIT AGAIN :)")
        elif ch==3:
            print("PAYING FOR MARINE VIEW")
            print("THANKYOU")
            print("VISIT AGAIN :)")
        else:
            print("INVALID CHOICE FOR PAYMENT MODE")
            cho=input("Do you want to try again? Y/N")
            if cho=="Y" or cho=="y":
                continue
            else:
                break
    print("*****PAYMENT WAS SUCCESSFULL****")




while True:
    print("1. BOOK YOUR ROOMS")
    print("2. ROOMS INFO")
    print("3. SERVICES")
    print("4. PAYMENT")
    print("5. RECORD")
    print("0. EXIT")
    ch=int(input("ENTER YOUR CHOICE"))
    if ch==1:
        print("Book your rooms")
        
    elif ch==2:
        room_info()
   
    elif ch==4:
        payment()
    
    elif ch==0:
        break
    else:
        print("INVALID CHOICE")