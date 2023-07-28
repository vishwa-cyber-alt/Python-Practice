from datetime import datetime
a=input("enter your name:")
dob=int(input("year:"))
y=datetime.now().year
c=y-dob;
print("Hi ",a)
print("your current age is ",c)
