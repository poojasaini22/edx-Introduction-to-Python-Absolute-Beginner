def quiz_item(question,solution):
    while True:
        if question==solution:
            print("correct")
            break
        else:
            put=input("enter again")
            if put==solution:
                print("correct 2")
                break
quiz_item(input("longest river in the world?"),"nile")
quiz_item(input("Number greater than 3?"),"4")
