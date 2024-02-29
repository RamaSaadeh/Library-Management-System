#student ID : F213886

import os
# Define the library as a dictionary
library = {}

# Define a function to add a book to the library
def add_book(book_id, book_genre, book_title, book_author, book_purchase_price, book_purchase_date):
  library[book_id] = {
    "genre": book_genre,
    "title": book_title,
    "author": book_author,
    "purchase_price": book_purchase_price,
    "purchase_date": book_purchase_date,
    "borrower_id": None,
    "reserved": False,
    "reserved_by": None
  }
import csv

# Open the text file and read the rows
with open('books_info.txt') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=':')
  for row in csv_reader:
    book_id = row[0]
    book_genre = row[1]
    book_title = row[2]
    book_author = row[3]
    book_purchase_price = row[4]
    book_purchase_date = row[5]

    # Add the book to the library
    add_book(book_id, book_genre, book_title, book_author, book_purchase_price, book_purchase_date)

# Set the file path to the text file containing the library information
file_path = "books_info.txt"

# Initialize an empty dictionary to store the library information
library = {}

# Function to load the library information from the text file
def load_library():
  if os.path.exists(file_path):
    with open(file_path, "r") as file:
      # Read each line in the file and split it into the book's information
      for line in file:
        book_info = line.strip().split(":")
        
        for info in book_info:
            info.strip()

        # Store the book information in the dictionary using the book's ID as the key
        add_book(book_info[0], 
                 book_info[1], 
                 book_info[2],
                 book_info[3],
                 book_info[4],
                 book_info[5])


    # Library Management System Log

# Define the log as a dictionary
log = {}

# Define a function to add a book to the library
def add_log(Lbook_id, Lmember_id, checkout_date, return_date, reservation):
  is_availble = True
  is_reserved = False
  if return_date == "-":
    is_availble = False
  if reservation != "-":
    is_reserved = True
  log[Lbook_id] = {
    "member id": Lmember_id,
    "checkout_date": checkout_date,
    "return date": return_date,
    "reservation":reservation,
    "available": is_availble,
    "borrower_id": None,
    "reserved": is_reserved,
    "reserved_by": None
  }
  
import datetime

def add_log_entry(book_id, member_id, checkout_date, return_date, reserved_by_member_id=None):
  # Create the log entry string
  log_entry = f"\n{book_id}:{member_id}:{checkout_date}:{return_date}"
  if reserved_by_member_id:
    log_entry += f":{reserved_by_member_id}"
  
  # Open the log file in append mode and write the log entry
  with open("log.txt", "a") as log_file:
    log_file.write(log_entry)
   
   
# Open the text file and read the rows
with open('log.txt') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=':')
  for row in csv_reader:
    Lbook_id = row[0]
    Lmember_id = row[1]
    checkout_date = row[2]
    return_date= row[3]
    reservation= row[4]

    # Add the log to the library
    add_log(Lbook_id, Lmember_id, checkout_date, return_date, reservation)

# Set the file path to the text file containing the log information
file_path2 = "log.txt"

# Initialize an empty dictionary to store the log information
log = {}

# Function to load the log information from the text file
def load_log():
  if os.path.exists(file_path2):
    with open(file_path2, "r") as file:
      # Read each line in the file and split it into the book's information
      for line in file:
        log_info = line.strip().split(":")
        
        for info in log_info:
            info.strip()
            
        # Store the book information in the dictionary using the book's ID as the key
        add_log(log_info[0], 
                 log_info[1], 
                 log_info[2],
                 log_info[3],
                 log_info[4])