"""Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output."""

# import array as arr
a = []

print("enter 5 numbers ")
for n in range(0, 5):
    ele = int(input(f"enter element number {n + 1} :"))
    a.append(ele)

a.sort()
print(f"sorted ascending :{a}")

a.sort(reverse=True)
print(f"sorted descending:{a}")
