"""Write a program that counts up the number of vowels [a, e, i , o,u] contained in the string."""

mystr = "my name is ayman "
ctr = 0
for char in mystr:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        ctr += 1
print(f"the number of vowels in the string is :{ctr}")
