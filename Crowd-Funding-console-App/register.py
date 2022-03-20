import re
# from home import home

def register(user_id=None):
    print("registration")
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
    # return home()
