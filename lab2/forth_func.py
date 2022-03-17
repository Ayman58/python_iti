"""Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not"""

def myforth_func():
    name=input("Enter your name")
    if name.isalpha() and len(name)!=0 :
        em=input("Enter your email")
        print(f"the name is:{name} \n the email is: {em} ")
    else:
        print("Enter a valid value")


myforth_func()