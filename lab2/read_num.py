"""Write a program which repeatedly reads numbers until the user
enters “done”.
Once “done” is entered, print out the total, count, and
average of the numbers.
If the user enters anything other than a number, detect their
mistake, print an error message and skip to the next number."""
def readnum ():
    myinput=" "
    coun=0
    avrg=0
    total=0
    while myinput !="done":
        myinput = input("Enter number")
        if myinput.isnumeric():
            num=int(myinput)
            coun+=num
            total+=1

        else:
            print("error")
    if myinput == "done":
        avrg = coun / total
        print(f"the count is:{coun} \n the total:{total} \n the average:{avrg}")

readnum()

