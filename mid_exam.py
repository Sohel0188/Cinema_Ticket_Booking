class star_cinema:
    hall_list=[]
    def enter_hall(self,hall):
        self.hall_list.append(hall)
   


class Hall(star_cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.enter_hall (self)
        super().__init__()
   
    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self.__show_list.append(show_info)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def book_seats(self,show_id,booking_seats):
        if show_id in self.seats:
            for row ,col in booking_seats:
                if 0 <= row < self.rows and 0 <= self.cols:
                    if self.seats[show_id][row][col]==0:
                        self.seats[show_id][row][col] = 1
                        print(f"Seat ({row},{col}) is booked successful")
                    else:
                        print(f"Seat ({row},{col}) is already booked.")
                else:
                    print(f"Seat ({row},{col}) is invalid for Show id {show_id}")

        else:
            print(f"Show Id {show_id} not found.")
    def view_show_list(self):
        for i in self.__show_list:
            print (i)

    def view_available_seats(self,show_id):
        if show_id in self.seats:
            print (f"Seat for Show id : {show_id}")
            for row in self.seats[show_id]:
                print(row)
        else:
            print(f"Show Id {show_id} not found.")

Star_Cinema = Hall(5,3,1)

Star_Cinema.entry_show(101,"The Godfather",'10:00 pm')
Star_Cinema.entry_show(102,"The Matrix",'01:00 pm')

option = True
while(option):

    print("1. View All Show Today")
    print("2. View Available Tickets")
    print("3. Book Tickets")
    print("4. Exit")

    number = int(input("Enter Option : "))

    if number ==1:
        Star_Cinema.view_show_list()
    elif number == 2:
        show_id = int(input("Enter show id : "))
        Star_Cinema.view_available_seats(show_id)
    elif number == 3:
        show_id = int(input("Enter show id : "))
        seat_no = int (input("Enter seat number which you want to book : "))
        booking_seats = []
        for i in range (seat_no):
            row = int(input("Enter row : "))
            col = int(input("Enter col : "))
            booking_seats.append((row,col))
        Star_Cinema.book_seats(show_id,booking_seats)
    else:
        option = False

        


