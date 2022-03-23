from home import home

# userid = 0


def login():
    print("######login#############")
    email = input("Enter your email")
    Pass = input("enter your password")
    try:
        with open("register.txt", "r") as myfile:
            userdata = myfile.readlines()
            for user in userdata:
                userinfo = user.strip("\n")
                userlist = userinfo.split(":")
                # print(userlist)
                # print(f"email:{userlist[3]}  , password :{userlist[4]}")
                if userlist[3] == email and userlist[4] == Pass:
                    print("login successfully ")
                    # global userid
                    user_id = userlist[0]
                    print(f"the id is :{user_id}")
                    return home(user_id)
            else:
                print("login failed ")
                return login()
    except Exception as e:
        print(e)


# def editUser():
#     with open("register.text", "r") as rfile:
#         data = rfile.readlines()
#
#     for user in data:
#         user = user.strip("\n")
#         userlist = user.split(":")
#         if userlist[0] == userid:
#             new_name = input("enter name ")
#             new_password = input("enter new password")
#             data = f"{new_name}:{new_password}"


# login()
