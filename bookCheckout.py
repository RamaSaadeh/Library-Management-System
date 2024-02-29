#student ID : F213886

import database
import datetime

# Define a function to checkout a book from the library
def checkout_book(book_id, member_id):
  database.load_library()
  database.load_log()
  # Check if the member ID is valid
  if not member_id.isdigit() or len(member_id) != 4 or int(member_id) < 1000 or int(member_id) > 9999:
    return "Invalid member ID"

  if book_id in database.library:

    #if book_id in database.library.keys() and\
    if database.log[book_id]["available"]:

      database.log[book_id]["available"] = False
      database.library[book_id]["borrower_id"] = member_id
      database.add_log(book_id, member_id, datetime.datetime.today().strftime("%d/%m/%Y"), 
      ("-"), ("-"))
      database.add_log_entry(book_id, member_id, datetime.datetime.today().strftime("%d/%m/%Y"), 
      ("-"), ("-"))

      return "Book checked out successfully"
    else:
        if database.log[book_id]["reservation"] != '-':
            database.library[book_id]["reservation"] = False
            return ("Book is not available and is reserved")
        else:
            return "Book is not currently available. Book available for reservation "
  else:
    return "Book not found in library"
  
  
def reserve_book(book_id, member_id):
  database.load_library()
  database.load_log()
  
  # Check if the member ID is valid
  if not member_id.isdigit() or len(member_id) != 4 or int(member_id) < 1000 or int(member_id) > 9999:
    return "Invalid member ID"
  
  
  # Reserve the book
  # Update the book's status
  if not database.log[book_id]["available"] and not database.log[book_id]["reserved"]:
    database.log[book_id]["available"] = False
    database.library[book_id]["borrower_id"] = member_id
    database.library[book_id]['reserved'] = True
    previous_borrower = database.log[book_id]["member id"]
    database.add_log(book_id, previous_borrower, 
                     datetime.datetime.today().strftime("%d/%m/%Y"), ("-"),member_id)
    database.add_log_entry(book_id, previous_borrower,
                           datetime.datetime.today().strftime("%d/%m/%Y"), ("-"),member_id)

  # Return True to indicate success
    return "Reserved sucessfully"
  else:
  # Return False to indicate failure
      return "Already reserved"