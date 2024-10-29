import tkinter as tk
from tkinter import messagebox

class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issued = False  # Tracks if the book is issued

class Library:
    def _init_(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x600")
        
        # Book inventory
        self.books = []
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Sets up the GUI layout"""
        tk.Label(self.root, text="Library Management System", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        # Frames for organization
        book_frame = tk.Frame(self.root)
        book_frame.pack(pady=10)
        
        # Book entry fields
        tk.Label(book_frame, text="Title:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(book_frame, font=("Helvetica", 12))
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(book_frame, text="Author:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(book_frame, font=("Helvetica", 12))
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(book_frame, text="ISBN:", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5)
        self.isbn_entry = tk.Entry(book_frame, font=("Helvetica", 12))
        self.isbn_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Buttons for book management
        tk.Button(self.root, text="Add Book", command=self.add_book, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.root, text="Update Book", command=self.update_book, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.root, text="Delete Book", command=self.delete_book, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.root, text="Issue Book", command=self.issue_book, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.root, text="Return Book", command=self.return_book, font=("Helvetica", 12)).pack(pady=5)
        
        # Display area
        self.book_list = tk.Listbox(self.root, width=60, height=10, font=("Helvetica", 10))
        self.book_list.pack(pady=10)
        
    def add_book(self):
        """Adds a new book to the library"""
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        
        # Validation
        if not title or not author or not isbn:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        # Create a new book and add to inventory
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        
        self.update_book_list()
        messagebox.showinfo("Book Added", f"{title} by {author} added to the library.")
        
        # Clear entries
        self.clear_entries()
        
    def update_book(self):
        """Updates the details of a selected book"""
        selection = self.book_list.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a book to update.")
            return
        
        selected_index = selection[0]
        book = self.books[selected_index]
        
        # Get updated information
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        
        if not title or not author or not isbn:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        # Update the book's details
        book.title = title
        book.author = author
        book.isbn = isbn
        self.update_book_list()
        
        messagebox.showinfo("Book Updated", f"{book.title} has been updated.")
        self.clear_entries()
        
    def delete_book(self):
        """Deletes a selected book from the library"""
        selection = self.book_list.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a book to delete.")
            return
            
        selected_index = selection[0]
        book = self.books[selected_index]
        
        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {book.title}?")
        if confirm:
            del self.books[selected_index]
            self.update_book_list()
            messagebox.showinfo("Book Deleted", f"{book.title} has been deleted.")
            self.clear_entries()
        
    def issue_book(self):
        """Issues a book based on the selected item in the list"""
        selection = self.book_list.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a book to issue.")
            return
            
        selected_index = selection[0]
        book = self.books[selected_index]
        
        if book.issued:
            messagebox.showwarning("Issue Error", "This book is already issued.")
        else:
            book.issued = True
            self.update_book_list()
            messagebox.showinfo("Book Issued", f"{book.title} has been issued.")
        
    def return_book(self):
        """Returns an issued book back to the library"""
        selection = self.book_list.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a book to return.")
            return
            
        selected_index = selection[0]
        book = self.books[selected_index]
        
        if not book.issued:
            messagebox.showwarning("Return Error", "This book is not issued.")
        else:
            book.issued = False
            self.update_book_list()
            messagebox.showinfo("Book Returned", f"{book.title} has been returned.")
    
    def update_book_list(self):
        """Updates the listbox display with the latest book information"""
        self.book_list.delete(0, tk.END)
        for book in self.books:
            status = "Issued" if book.issued else "Available"
            self.book_list.insert(tk.END, f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")
    
    def clear_entries(self):
        """Clears the entry fields after adding, updating, or deleting a book"""
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)

# Run the application
root = tk.Tk()
app = Library(root)
root.mainloop()

