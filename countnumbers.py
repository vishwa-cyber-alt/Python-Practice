L = [1, 5, 7, 3, 9, 5, 5, 9, 7, 9]
n = int(input("Enter number to count:"))
count = 0
for i in L:
    if i == n:
        count += 1
print(f"The number {n} appears {count} times in the list.")
