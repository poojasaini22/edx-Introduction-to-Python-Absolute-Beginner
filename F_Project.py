def adding_report(arg):
    if arg=="A".lower():
        print("Input an integer to add to the total or \"Q\" to quit")
        total=0
        item="0\n"
        add=0
        while True:
            add=(input("Enter an integer or 'Q'").lower())
            if add.isdigit()==True:
                item+=(add +"\n")
                total+=int(add)
            elif add.startswith("q")==True:
                break
            else:
                print(add,"is invalid input")
        print("items")
        print(item)
        print("total")
        print(total)

    elif arg=="T".lower():
        print("Input an integer to add to the total or \"Q\" to quit")
        total=0
        sum=0
        while True:
            sum=input("Enter an integer or 'Q'").lower()
            if sum.isdigit()==True:
                total+=int(sum)
            elif sum.startswith("q")==True:
                break
            else:
                 print(sum,"is invalid input")
        print("total")
        print(total)
    else:
        adding_report(input("enter 'A' or 'T'"))

adding_report(input("enter 'A' or 'T'").lower())
