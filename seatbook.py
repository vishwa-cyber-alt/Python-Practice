seat_booked=[1,3,5,7,9,11]
seat_notbooked=[2,4,6,8,10]
etb=int(input("enter to book="))
if etb in seat_booked:
    print("already booked")
elif etb in seat_notbooked:
    print("notbooked")
    seat_booked.append(etb)
    print("your seat ",etb,"success")
    print(seat_booked)
else:
    seat_booked.append(etb)
    print("your seat ",etb,"success")
    print(seat_booked)
