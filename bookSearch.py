#student ID : F213886

import database

# Function to search for a book in the library by title
def search_book(title):
  # Load the library information from the text file
  database.load_library()
  
  # Search for the book in the library
  for book_id, book_info in database.library.items():
    if str.lower (title) in str.lower (book_info["title"]):
      # Display the book information if the book is found
      return f"""Book ID: {book_id}
Genre: {book_info['genre']}
Title: {book_info['title']}
Author: {book_info['author']}
Purchase price: {book_info['purchase_price']}
Purchase date: {book_info['purchase_date']}"""
      break
  else:
    # Display a message if the book is not found
    return f"No book with the title '{title}' was found in the library."