"""Write a program that remove all vowels from the input word and generate a brief version of it."""

str=" ayman "
str.strip("aeiou ")

vowels = ['a','e','i','o','u']
result = [letter for letter in str if letter.lower() not in vowels]
result = ''.join(result)
print(result)
