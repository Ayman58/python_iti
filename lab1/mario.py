"""Write a program that build a Mario pyramid like below:"""
# rows = int(input("Enter number of rows: "))
rows=4
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")