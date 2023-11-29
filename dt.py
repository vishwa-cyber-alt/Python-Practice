from datetime import datetime
a=int(input("press 1 to get date , press 2 to get time \n"))
now = datetime.now()
if a==1:
	print("date")
	dt_string = now.strftime("%d/%m/%Y")
	print(dt_string)
elif a==2:
	print("time")
	t=now.strftime("%H:%M:%S")
	print(t)
