class Train:
    def __init__(self, name, price, seats):
        self.name = name
        self.price = price
        seat = []
        for i in range(1, seats+1):
            seat.append(i)
        seat.sort()
        self.seats = seat

    def getstatus(self):
        print(
            f"Name of the train is {self.name} and no of seats available are {self.seats} \n")

    def fare(self):
        print(f"Fare of {self.name} is {self.price}")

    def bookTicket(self, seat_no):
        if (len(self.seats) > 0):
            if seat_no in self.seats:
                self.seats.remove(seat_no)
                self.seats.sort
                print(
                    f"Your ticket is booked and your seat no is {seat_no} \n ")
                print(f"Available seats are now {self.seats}\n")    
            else:
                print("This ticket is already booked")
        else:
            print("Sorry!!! All seats are booked")

    def cancelTicket(self, seat_no):
        if seat_no in self.seats:
            print("Your ticket is already been cancelled")
        else:
            print("Your ticket has been cancelled")
            self.seats.append(seat_no)
        self.seats.sort()
        print(f"Available seats are {self.seats}")

    @staticmethod
    def greet():
        print("*****Welcome to Indian Railways***** \n")


kalindiExpress = Train("Kalindi", 400, 5)

kalindiExpress.greet()
kalindiExpress.getstatus()
kalindiExpress.bookTicket(5)
kalindiExpress.cancelTicket(1)
