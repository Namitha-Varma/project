class InvalidTicketCount(Exception):
    def __init__(self, msg):
        msg = f"Invalid Tickets Count"
        super().__init__(msg)

class SeatsNotAvailable(Exception):
    def __init__(self, msg):
        msg = f"Requested seats are not available"
        super().__init__(msg)

class BookingLimitExceeded(Exception):
    def __init__(self, msg):
        msg = f"Booking limit exceeded"
        super().__init__(msg)

class BookingException(Exception):
    """Base class for booking-related exceptions"""
    pass

def book_tickets(available_seats, max_booking_limit,):
    try:
        
        tickets = int(input("Enter number of tickets to book: "))
    
        
        if tickets <= 0:
            raise InvalidTicketCount(f"enter valid ticket count :")
            
        if tickets > available_seats:
            raise SeatsNotAvailable("Not enough seats available")
        
        if tickets > max_booking_limit:
            raise BookingLimitExceeded(f"You can book maximum {max_booking_limit} tickets only")
        
       
        available_seats -= tickets
        print("Booking successful")
        print("Remaining seats:", available_seats)


        print("Available Seats:", available_seats)
        print("Maximum tickets per booking:", max_booking_limit)

    except (ValueError, TypeError):
        print("Please enter numeric values only")

    except Exception as e:
        print(e)

    finally:
        print("Booking session ended")



available_seats = 50
max_booking_limit = 5

print("Available Seats:", available_seats)
print("Maximum tickets per booking:", max_booking_limit)
book_tickets(available_seats, max_booking_limit)

    

