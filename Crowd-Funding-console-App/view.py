"""User can view all projects"""
import os
# from home import home


def view():
    for x in os.listdir():
        if x.endswith(".txt"):
            print(x)

    fileName = input("enter project  name :")
    try:
        with open(fileName + ".txt", "r") as myfile:
            print(myfile.read())
            # return home()
    except Exception as e:
        print(e)

# view()
