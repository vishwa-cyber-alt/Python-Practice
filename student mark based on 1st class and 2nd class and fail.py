m = int(input("How many marks do you want to enter: "))
ma = []

for i in range(0, m):
    mark = int(input("Enter the mark: "))
    ma.append(mark)

print("Entered marks:", ma)

grades = []
for mark in ma:
    if mark >= 80:
        grades.append("first class")
    elif mark>60:
        grades.append("second class")
    elif mark<25:
        grades.append("Fail")

c = 0  # Initialize the counter for "Fail"
a = 0  # Initialize the counter for "A grade"
sc=0

for grade in grades:
    if grade == "Fail":
        c += 1
    elif grade == "first class":
        a += 1
    elif grade == "second class":
        sc += 1

print("Number of Fail grades:", c)
print("Number of first class:", a)
print("Number of second class:", sc)
print("Grades:", grades)
