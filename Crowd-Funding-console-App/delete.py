"""User can delete his own project"""
import os

# from home import home

def delete(userid):
    for files in os.listdir():
        if files.endswith(".txt"):
            print(files)

    file_name = input("Enter the file that u want to delete ")
    try:
        with open(file_name + ".txt", "r") as myfile:
            getid = myfile.readline()
            myfile.close()
            checkid = int(getid.strip("\n"))
            if userid == checkid:
                try:
                    os.remove(file_name + ".txt")
                    # return home()
                except Exception as e:
                    print(e)
                else:
                    for x in os.listdir():
                        if x.endswith(".txt"):
                            print(x)
            else:
                print("you can only delete your own files  ")
    except Exception as e:
        print(e)

# delete(1)
