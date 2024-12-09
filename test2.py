import sys
L = []
print("if you want stop the program enter stop!")
while True:
    first = input(f'what do you want to do?\n choose from ADD , Update , delete , List \n')
    L1 = ["Add" , "Update" , "delete" , "List"]
    if first not in L1 :
        print("choos the correct item!")
        continue 
    print("If you regret it and want to go back to the first page, print back!")
    if first == "back" :
        break
    if first == "stop" :
        sys.exit()
    if first == "Add" :
        print('enter a name ==> <name>')
        Add = input("your name ==> ")
        L.append(Add)
        for i in L :
            print(f'<{i}>')
    if first == "Update" : 
        while True:
                print("your change ==> <change>")
                Update = input("enter your change ==> ")
                if Update == Add :
                    print(f'The name already exists!\n pleas enter another name:\n')
                    continue
                if len(L) > 0 :
                    index = L.index(Add)
                    L[index]=Update
                    for i in L :
                        print(f'<{i}>') 
                else :
                    print("List is empty!")
                if len(L) > 0 :
                    break 
    if first == "delete" :
        while True :
                delete = input(f'enter whatever you want to delete ==>\n')
                if delete not in L :
                    print(f'{delete} Does not exist!')
                    continue
                if delete in L :
                    L.remove(delete)
                    print(f'delete {delete} succes') 
                    for i in L :
                        print(f'your list is ==> <{i}>')
                    break
                else :
                    print("List is empty!") 
    if first == "List" :
        print(L) 
