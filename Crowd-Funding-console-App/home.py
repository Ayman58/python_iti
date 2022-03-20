from creatProject import creatproject
from view import view
from delete import delete
from edit import edit

def home(userid):
    print("the home Page ")
    choice = input("Enter (c) to create new project \n(v) to view all projects \n(d) to delete your project\n(e) to "
                   "edit\n")
    if choice == "c":
        return creatproject(userid)
    elif choice == "v":
        return view()
    elif choice == "d":
        return delete(userid)
    elif choice == "e":
        return edit(userid)
    else:
        return home()


# home()
