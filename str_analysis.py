#Create the str_analysis() function that takes a string argument. In the body of the function:
#Program: str_analysis() Function
def str_analysis(arg):
    while True:
        if arg=="":
            str_analysis(input("enter"))
            break
        elif arg.isdigit()==True:
            if int(arg)<=99:
                print(arg,"smaller number than expected")
                break
            else:
                print(arg,"is a pretty big number")
                break
        elif arg.isalpha()==True:
            print(arg,"is all alphabetical character")
            break
        else:
            print(arg,"is neither all digit characters nor all alpha")
            break


str_analysis(input("enter"))
