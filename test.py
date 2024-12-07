L = []
print("if you want stop the program enter stop!")
while True:
    x = input(f'what do you want to do?\n choose from ADD , Update , delete \n' )
    if x == "stop" :
        break 
    if x == "Add" :
        print("if you want to exit , type exit!")
        while True:
            Add = input("Add something to List ==>")
            if Add == "exit" :
                break
            L.append(Add)
        print(L) 
        continue    
    if x == "Update" and len(L) > 0 :
        previous_value = input("enter your previous value you want change ==>")
        new_value = input("enter your new value ==>")
        if previous_value in L :
            index = L.index(previous_value)
            L[index]=new_value
        else:
            print("can not found this value in your list")
        if previous_value in L :
            L.remove(previous_value)
    else :
        print("List is empty")
    print(L)
    if x == "delete" and len(L) > 0 :
        delete = input("enter something you want to delet==> ")
        L.remove(delete)
    else :
        print("List is empty")    
    print(L)