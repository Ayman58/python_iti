"""Write a program that prints the locations of " i " character in any string you added."""

str = "dhdbsbinsin i ijsn shdhi "

for n in range(len(str)):
    if str[n]=="i":
        print(n)

