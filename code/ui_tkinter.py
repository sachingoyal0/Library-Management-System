# Tkinter-based GUI code
# 4. ui_tkinter.py
import tkinter as tk
from manage_books import add_book

def add_book_ui():
    """GUI for adding a book."""
    root = tk.Tk()
    root.title("Add Book")

    tk.Label(root, text="Title").grid(row=0)
    tk.Label(root, text="Author").grid(row=1)
    tk.Label(root, text="Category").grid(row=2)
    tk.Label(root, text="Available Copies").grid(row=3)

    # Input fields
    title = tk.Entry(root)
    author = tk.Entry(root)
    category = tk.Entry(root)
    available = tk.Entry(root)

    title.grid(row=0, column=1)
    author.grid(row=1, column=1)
    category.grid(row=2, column=1)
    available.grid(row=3, column=1)

    status_label = tk.Label(root, text="", fg="red")
    status_label.grid(row=5, column=1)

    # Submit button functionality
    def submit():
        try:
            available_copies = int(available.get())
            if not title.get() or not author.get() or not category.get() or available_copies <= 0:
                raise ValueError("Please fill all fields with valid data.")
            add_book(title.get(), author.get(), category.get(), available_copies)
            status_label.config(text="Book added successfully!", fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")

    tk.Button(root, text="Submit", command=submit).grid(row=4, column=1)

    root.mainloop()

if __name__ == "__main__":
    add_book_ui()


# **Errors are red ❤️, databases are blue 💙, writing love queries 💻💌, this is for you! 🥰✨**