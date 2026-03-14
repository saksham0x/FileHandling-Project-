from pathlib import Path

exitbtn = True

while exitbtn == True:
    def ShowFiles():
        path = Path('')
        items = list(path.rglob('*'))
        for i , item in enumerate(items):
            print(f"{i+1} : {item}")

    def CreateFile():
        ShowFiles()

        FileName = input("plese enter your File Name : ")
        with open(FileName, 'w') as fs:
            data = input("What your want to wright in this file : ")
            fs.write(data)

        print("Create file is susscesfully ! ")

    def readFiles():
        ShowFiles()
        path = Path('')
        items = list(path.rglob('*'))
        no = int(input("Enter your File number to read as file ! "))
        with open(items[no-1]) as read:
            c = read.read()
            print(c)

    def AppendFile():
        ShowFiles()
        path = Path('')
        items = list(path.rglob('*'))
        no = int(input("enter File number: "))
        data = input("Enter append Data : ")
        with open(items[no-1],'a+') as a:
            a.write(data)
            a.seek(0)
            print(a.read())

    def DeleteFile():
        ShowFiles()
        path = Path('')
        items = list(path.rglob('*'))
        no = int(input("enter File number: ")) 
        file = items[no-1]
        if file.exists:
            file.unlink()
            print("File delete sussesfully ! ")
        else:
            print("file not found !")

    def menu():
        print("******Plese only using file ! ******** if you use folder so show meny errors! ***")
        print("press 1 for Create A file : ")
        print("press 2 for read A file : ")
        print("press 3 for wright A file : ")
        print("press 4 for Delete A file : ")
        print("Press 5 to exit !.. :")
        chick = int(input("plese enter your response :- "))
        return chick

    chick = menu()

    if chick == 1:
        CreateFile()

    elif chick == 2:
        readFiles()
    elif chick == 3:
        AppendFile()
    elif chick == 4:
        DeleteFile()
    elif chick == 5:
        exitbtn = False
        break
    else:
        print("Your choice is not Found ! plese try again !")