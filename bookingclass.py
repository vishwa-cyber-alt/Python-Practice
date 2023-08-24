class Booking:
    def __init__(self,carname,carcolor):
        self.carname=carname
        self.carcolor=carcolor
    def print(self):
        print("Car Name : ",self.carname)
        print("color:",self.carcolor)
book=Booking("Ferrari","red")
book.print()
