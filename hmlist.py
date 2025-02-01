import time
listo = [[],[]] #
while True:
    list = int(input("What would you like to do? \n1 - Add a name to the list \n2 - Change a name in the list \n3 - View all names in the list \n4 - Delete a name in the list \n5 - Exit \n "))
    
    if list==1:
        add = input("What would you like to add?")
        listo.append(add)
        print(listo)
        time.sleep(2)
    elif list==2:
        print(listo)
        cha = int(input("What name would you like to change?"))
        
        time.sleep(2)
    elif list==3:
        print(listo)
        time.sleep(2)
    elif list==4:
        rem = input("What would you like to remove?")
        listo.remove(rem)
        time.sleep(2)
    elif list==5:
        time.sleep(1.5)
        print("Exiting...")
        break
    else:
        print("Invalid number! Try again.")
