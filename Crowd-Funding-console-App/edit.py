"""User can edit his own projects"""
import os

from creatProject import checkDate
# from home import home

def edit(userid):
    for files in os.listdir():
        if files.endswith(".txt"):
            print(files)

    file_name = input("Enter the file that u want to edit ")
    try:
        with open(file_name + ".txt", "r") as myfile:
            getid = myfile.readline()
            myfile.close()
            checkid = int(getid.strip("\n"))
            if userid == checkid:
                title = input("Set Title For Your Project:")
                details = input("Details:")
                target = input("Target Money:")
                StartDate = checkDate(input("enter Start Date"))
                EndDate = checkDate(input("enter End Date"))

                p_data = f"{str(userid)}\n{title}\n{details}\n{target}\n{StartDate}\n{EndDate}\n"
                try:
                    pfile = open(file_name + ".txt", 'w')
                    print("Edite done successfully ")
                except Exception as e:
                    print(e)
                else:
                    pfile.write(p_data)
                    pfile.close()
                    # return home()

            else:
                print("u only can edit your projects ")
                edit(userid)
    except Exception as e:
        print(e)

# edit(1)