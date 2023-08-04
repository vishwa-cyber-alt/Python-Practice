seat_booked=[1,3,5,7,9,11]
seat_notbooked=[2,4,6,8,10]
n=3
for i in range(0,n+1):
    availability=int(input("enter to check availability="))
    if availability in seat_booked:
         print("booked")
    elif availability in seat_notbooked:
         print("notbooked")
