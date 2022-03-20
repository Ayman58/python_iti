"""The user can create a project fund raise campaign which contains:
• Title
• Details
• Total target (i.e 250000 EGP)
• Set start/end time for the campaign (validate the date formula)"""
from datetime import datetime


def creatproject(userid):
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


formatt = "%d/%m/%Y"


def checkDate(date):
    try:
        res = (datetime.strptime(date, formatt))
    except ValueError:
        print("please write valid date i.e. (D/M/Y)1/1/2020")
        checkDate()
    return date
    print(res)


# creatproject(1)
# checkDate("1-1-2020")
