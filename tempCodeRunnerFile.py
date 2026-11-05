def deletefile() :
    try :
        readfileandfolder()
        name = int(input("Which file you want to delete : "))
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)

            print("File removes successfully")

        else :
            print("No such file exist")

    except Exception as err:
        print(f"An error occured as {err}")