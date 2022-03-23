# from creatProject import creatproject
# from view import view
# from delete import delete
# from edit import edit

from datetime import datetime
import os
from creatProject import checkDate
import re

userid = 0


def register(user_id):
    print("########  registration ###########")
    # user_id+=1
    Fname = input("Enter your first name ")
    Lname = input("Enter your last name ")
    email = input("Enter your email ")
    password = input("Enter your password ")
    confirm = input("confirm your password ")
    if not confirm == password:
        print("the password is not the same ")
        return register()
    phone = input("Enter your phone number ")

    if not re.fullmatch("^01[0125][0-9]{8}$", phone):
        print("Enter a valid phone number")
        return register()

    reg_file = open("register.txt", "a")
    data = f"{user_id}:{Fname}:{Lname}:{email}:{password}:{phone}\n"

    reg_file.write(data)
    reg_file.close()
    return home(user_id)


def home(user_id):
    print(f"################### the home Page #################(id{user_id})####### ")
    choice = input("Enter (c) to create new project \n(v) to view all projects \n(d) to delete your project\n(e) to "
                   "edit\n -------------------------------------------\n")

    # global userid
    userid = int(user_id)
    if choice == "c":
        return creatproject(userid)
    elif choice == "v":
        return view(userid)
    elif choice == "d":
        return delete(userid)
    elif choice == "e":
        return edit(userid)
    else:
        return home(userid)


def creatproject(userid):
    print(f"######## creat project #########(id{userid})########")
    title = input("Set Title For Your Project:")
    details = input("Details:")
    target = input("Target Money:")

    StartDate = checkDate(input("enter Start Date"))
    EndDate = checkDate(input("enter End Date"))
    pname = f"{title}.txt"

    p_data = f"{str(userid)}\n{title}\n{details}\n{target}\n{StartDate}\n{EndDate}\n"
    try:
        pfile = open(pname, 'w')
    except Exception as e:
        print(e)
    else:
        pfile.write(p_data)
        pfile.close()
        print("done :) ")

    return home(userid)


formatt = "%d/%m/%Y"


def checkDate(date):
    try:
        res = (datetime.strptime(date, formatt))
    except ValueError:
        print("please write valid date i.e. (D/M/Y)1/1/2020")
        edit(userid)
    return date
    print(res)


def view(userid):
    print("*********the available projects **************")
    for x in os.listdir():
        if x.endswith(".txt"):
            print(x)
    print(f"********************************(id{userid})*****")
    fileName = input("enter project  name to view:")
    try:
        with open(fileName + ".txt", "r") as myfile:
            print("-------------------------------------------------------")
            print(myfile.read())
            print("-------------------------------------------------------")
            return home(userid)
    except Exception as e:
        print(e)
    return home(userid)


def delete(userid):
    print(f"######### the available projects ###########(id{userid})#######")
    for files in os.listdir():
        if files.endswith(".txt"):
            print(files)
    print("####################################################")
    file_name = input("Enter the file that u want to delete:")
    try:
        with open(file_name + ".txt", "r") as myfile:
            getid = myfile.readline()
            myfile.close()
            checkid = int(getid.strip("\n"))
            if userid == checkid:
                try:
                    os.remove(file_name + ".txt")
                    print("done ")
                    return home(userid)
                except Exception as e:
                    print(e)
                    for x in os.listdir():
                        if x.endswith(".txt"):
                            print(x)
            else:
                print("you can only delete your own files  ")
    except Exception as e:
        print(e)


def edit(userid):
    print("######### the available projects ##################")
    for files in os.listdir():
        if files.endswith(".txt"):
            print(files)
    print(f"###########################################(id{userid})#########")
    file_name = input("Enter the file that u want to edit ")
    try:
        with open(file_name + ".txt", "r") as myfile:
            getid = myfile.readline()
            myfile.close()
            checkid = int(getid.strip("\n"))
            # print(type(userid))
            # print(type(checkid))
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
                    return home(userid)

            else:
                print("u only can edit your projects ")
                edit(userid)
    except Exception as e:
        print(e)
