"""Write a program that generate a multiplication table from 1 to the number passed."""
num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)