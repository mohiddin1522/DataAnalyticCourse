while(True):
    print("enter your choice: ")
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. exit")
    choice = int(input())
    if(choice == 1):
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print(a+b)
        print(f"would you like to continue?")
        print("1. yes")
        print("2. no")
        cont = int(input())
        if(cont == 1):
            continue
        else:
            print("exiting...")
            break
        
    elif(choice == 2):
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print(a-b)
        print(f"would you like to continue?")
        print("1. yes")
        print("2. no")
        cont = int(input())
        if(cont == 1):
            continue
        else:
            print("exiting...")
            break
        
    elif(choice == 3):
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print(a*b)
        print(f"would you like to continue?")
        print("1. yes")
        print("2. no")
        cont = int(input())
        if(cont == 1):
            continue
        else:
            print("exiting...")
            break
        
    elif(choice == 4):
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print(a/b)
        print(f"would you like to continue?")
        print("1. yes")
        print("2. no")
        cont = int(input())
        if(cont == 1):
            continue
        else:
            print("exiting...")
            break
        
    elif(choice == 5):
        print("exiting...")
        break
    else:
        print("invalid choice")