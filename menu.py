#student ID : F213886

import bookCheckout
import bookSearch
import bookReturn
import bookSelect
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Display menu
window = tk.Tk()
window.title("Library Management System")
window.geometry("1150x600")

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)
right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT)


frame = tk.Frame(master=left_frame, width=35, height=35).pack()


# Get user input
def show_search_results():
    global search_results
    book_title= search_input.get()
    results = bookSearch.search_book(book_title)
    search_results.configure(text=results)


# Process user input
  # Search for books
search_input = tk.StringVar()
search_bar_label=tk.Label(text="Search Book Titles:",background="grey", foreground="black",
                          font=("lucida",15) ).pack()
search_bar = tk.Entry(window, fg="white", bg="black", width=50, textvariable=search_input).pack()
search_results=tk.Label(window, text="")
search_results.pack()

search_button = tk.Button(window,
    text="Search",
    bg="white",
    fg="black",
    command=show_search_results
).pack()


# Design Spacing using frames and separators
frame = tk.Frame(master=left_frame, width=35, height=35).pack()
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x')
frame = tk.Frame(master=left_frame, width=35, height=35).pack()

# Checkout Books
def checkout_books():
    global checkout_results
    book_id= bookid_input.get()
    member_id=memberid_input.get()
    results2 = bookCheckout.checkout_book(book_id,member_id)
    checkout_results.configure(text=results2)
    
def reserve_books():
    global reserve_results
    book_id= bookid_input.get()
    rsrv=rsrv_input.get()
    results4 = bookCheckout.reserve_book(book_id,rsrv)
    reserve_results.configure(text=results4)


bookid_input = tk.StringVar()
memberid_input = tk.StringVar()
rsrv_input = tk.StringVar()
checkout_label=tk.Label(text="Checkout Books", background="grey", foreground="black",
                        font=("lucida",15) ).pack()
frame = tk.Frame(master=left_frame, width=15, height=15).pack()
bookid_bar_label=tk.Label(text="Book ID").pack()
book_id_bar=tk.Entry(window, fg="white", bg="black", width=50, textvariable=bookid_input).pack()
memberid_bar_label=tk.Label(text="Member ID").pack()
member_id_bar=tk.Entry(window, fg="white", bg="black", width=50, textvariable=memberid_input).pack()
checkout_results=tk.Label(window, text="")
checkout_results.pack()

checkout_button = tk.Button (window, 
text="Check Out",
bg="white",
fg="black",
command=checkout_books
).pack()

frame = tk.Frame(master=left_frame, width=15, height=15).pack()
reserve_bar_label=tk.Label(text="Reservation Member ID").pack()
reserve_bar=tk.Entry(window, fg="white", bg="black", width=50, textvariable=rsrv_input).pack()
reserve_bar_not=tk.Label(
    text="Please note the reservation will only be held for 7 days after the book becomes available", 
                         font=("lucida",10)).pack()

reserve_results=tk.Label(window, text="")
reserve_results.pack()

reserve_button = tk.Button (window, 
text="Reserve",
bg="white",
fg="black",
command=reserve_books
).pack()


# Design Spacing using frames and separators
frame = tk.Frame(master=left_frame, width=35, height=35).pack()
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x')
frame = tk.Frame(master=left_frame, width=35, height=35).pack()

# Return Books

def return_books():
    global return_results
    book_id2= bookid_input2.get()
    results3 = bookReturn.return_book(book_id2)
    return_results.configure(text=results3)

bookid_input2 = tk.StringVar()
return_label=tk.Label(text="Return Books", background="grey", foreground="black", 
                      font=("lucida",15) ).pack()
frame = tk.Frame(master=left_frame, width=15, height=15).pack()
bookid_bar_label3=tk.Label(text="Book ID").pack()
book_id_bar2=tk.Entry(window, fg="white", bg="black", width=50, textvariable=bookid_input2).pack()
return_results=tk.Label(window, text="")
return_results.pack()

return_button = tk.Button (window, 
text="Return Book",
bg="white",
fg="black",
command=return_books
).pack()

# Implementing Book Select function
def show_data():
    global data
    fig, ax = plt.subplots()
    genre_frequency = bookSelect.generate_freq()
    ax.bar(genre_frequency.keys(), genre_frequency.values())
    ax.set_title("Most Checked Out Books by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Number of Books")
    plt.xticks(rotation=45)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, right_frame)
    canvas.get_tk_widget().pack()

    return canvas
    # data_results = bookSelect.generate_freq(frequency)
    # data_results.configure(text=data_results)

show_data2 = tk.StringVar()
data_label=tk.Label(right_frame, text="Book Purchasing Data", background="grey", foreground="black", 
                      font=("lucida",15) ).pack()
frame = tk.Frame(master=right_frame, width=15, height=15).pack()

data_button = tk.Button (right_frame,
text="Show Data Results",
bg="white",
fg="black",
command=show_data
).pack()

# Implementing Function to show top 5 most checked out books
def suggest_popular_books():
    global suggest_results
    checkout_freq = bookSelect.suggest()
    results5 = bookSelect.suggest()
    suggest_results.configure(text=results5)

data_button = tk.Button (right_frame,
text="Most Popular Books",
bg="white",
fg="black",
command=suggest_popular_books
).pack()

suggest_results=tk.Label(right_frame, text="")
suggest_results.pack()

# Implementing function to suggest budget for repurchasing more copies of top 5 books

def suggest_budget():
    global budget_results
    budget_freq = bookSelect.budget()
    results6 = bookSelect.budget()
    budget_results.configure(text=results6)

budget_button = tk.Button (right_frame,
text="Book Purchase Budget",
bg="white",
fg="black",
command=suggest_budget
).pack()

budget_bar_not=tk.Label(right_frame,
    text="Suggested budget for purchasing more copies of most popular books (in GBP)", 
                         font=("lucida",10)).pack()

budget_results=tk.Label(right_frame, text="")
budget_results.pack()

window.mainloop()