m = int(input("How many marks do you want to enter: "))
ma = []

for i in range(0, m):
    mark = int(input("Enter the mark: "))
    ma.append(mark)

print("Entered marks:", ma)

grades = []
for mark in ma:
    if mark >= 80:
        grades.append("A grade")
    else:
        grades.append("Fail")

print("Grades:", grades)
