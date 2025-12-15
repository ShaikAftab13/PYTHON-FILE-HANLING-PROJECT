import os
from pathlib import Path

def read_file_and_folder():
    path=Path('')
    items=list(path.rglob("*"))
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")

def create_file():
    try:
        read_file_and_folder()
        name=input("Please tell your file name:-")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("What you want to write in this file:-")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")

        else:
            print(f"This file already exists")

    except Exception as e:
        print(f"An exception occurred : {e}")

def read_file():
    try:
        read_file_and_folder()
        name=input("Which file you want to read:-")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)

            print("FILE READED SUCCESSFULLY ")
        else:
            print("File doesn't exists")

    except Exception as e:
        print(f"An error occurred : {e}")

def update_file():
    try:
        read_file_and_folder()
        name=input("Tell which file you want to update:-")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the date of your file")
            print("Press 3 for appending some content in your file")
            res=int(input("Enter your response:"))
            if res==1:
                name1=input("Tell your new file name:")
                p2=Path(name1)
                p.rename(p2)
                print("FILE NAME CHANGED SUCCESSFULLY")
            if res==2:
                with open(p,"w") as fs:
                    data=input("Enter what you want to write (Note: This will overwrite your data)")
                    fs.write(data)
                print("FILE CONTENT OVERWRITTED SUCCESSFULLY")
            if res==3:
                with open(p,"a") as fs:
                    data=input("Enter the content you want to append:")
                    fs.write(" ",data)
                print("NEW CONTENT APPENDED SUCCESSFULLY")
        else:
            print("File doesn't exists")
    except Exception as e:
        print(f"An exception occurred : {e}")

def delete_file():
    try:
        read_file_and_folder()
        name=input("Enter the name of file ,you want to delete:-")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("No such file exists")
    except Exception as e:
        print(f"An exception occurred : {e}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

choice=int(input("Enter your response:"))

match choice:
    case 1:
        create_file()
    case 2:
        read_file()
    case 3:
        update_file()
    case 4:
        delete_file()