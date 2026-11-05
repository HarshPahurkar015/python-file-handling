from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = [
        item for item in list(path.rglob('*'))
        if '.git' not in item.parts
    ]

     #rglob() -> helps to search for files and directories recursively # rglob(*) -> recursively find everything under this path
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try :
        readfileandfolder()
        name = input("Please tell your file name : ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file : ")
                fs.write(data)

            print(F"{name} FILE CREATED SUCCESSFULLY")
        else :
            print("this file already exist")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try :
        readfileandfolder()
        name = input("which file you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("Read successfully")
        else :
            print("the file does not exist")
    except Exception as err:
       print(f"An error occurred as {err}")

def updatefile():
    try : 
        readfileandfolder()
        name = input("Tell which file you want to update : ")
        p = Path(name)
        if p.exists and p.is_file() :
            print("Press 1 for changing the name of your file : ")
            print("Press 2 for overwriting the data of your file")
            print("press 3 for appending some content in your file")

            res = int(input("Tell your response : "))

            if res == 1 :
                name2 = input("Tell your new file name : ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write this is overwirte the data : ")
                    fs.write(data)

            if res == 3 :
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append : ")
                    fs.write(" " +  data)
    except Exception as err:
        print(f"an error occured as {err}")

def deletefile() :
    try :
        readfileandfolder()
        name = (input("Which file you want to delete : "))
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)

            print("File removes successfully")

        else :
            print("No such file exist")

    except Exception as err:
        print(f"An error occured as {err}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for delete a file")

check = int(input("Please check your response : "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4 :
    deletefile()