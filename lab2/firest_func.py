"""Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start."""

def myFirstFunc(len, start):
    newl = []
    for i in range(start,len):

       newl.append(i)
    print(newl)

myFirstFunc(5,2)