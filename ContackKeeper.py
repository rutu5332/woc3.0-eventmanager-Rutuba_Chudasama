print("\n\t\tHello \n  Welcome to Contact Keeper")
contacts = [ ]
flag = 1


while flag:
    print("\n********************************************************")
    print("Select you Choice : ")
    choice = input(" 1:Add new Number \n 2:Display\n 3:Exit\nChoice => ")
    if choice=="1" :
        name = input("\nEnter the name of Contact : ")
        con = input("Enter Contact No : ")
        ch='y'
        while ch=='y' or ch == 'Y':
            ch = input("\nDo you want to add one more contact to " + name + " ?[y/n] : ")
            if ch == 'y' or ch =='Y':
                tmp = input("Enter Contact No : ")
                con += ','+tmp
        tup = (name , con )
        contacts.append(tup)
        contacts.sort()
    elif choice=="2":
        print("\n--------------------------------------------")
        print("\tYour Contacts ")
        for c in contacts:
            print(c[0] + " : " +c[1])
        print("--------------------------------------------")
    else:
        print("******** Thank You *********\n")
        flag = 0

