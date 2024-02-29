#student ID : F213886

import database
import datetime

# Define a function to return a book to the library

def return_book(book_id):
    database.load_log()
    database.load_library()
    
    
    if book_id in database.library:
        if book_id in database.log.keys() and database.log[book_id]["return date"] == "-":
            database.log[book_id]["available"] = True

            reservation = "-"
            for log_book_id in database.log:
                if book_id==log_book_id:
                    previous_borrower = database.log[book_id]["member id"] 
                    reservation = database.log[book_id]["reservation"]
                    break
            database.add_log(book_id, previous_borrower, ("-"),
                             datetime.datetime.today().strftime("%d/%m/%Y"), reservation)
            database.add_log_entry(book_id, previous_borrower, ("-"), 
                                   datetime.datetime.today().strftime("%d/%m/%Y"), reservation)

            
            return "Book returned successfully"
        else:
            return "Book is already available"
    else:
        return "Book not found in library"