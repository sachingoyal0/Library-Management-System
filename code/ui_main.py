# Main file to run the UI (Optional: Tkinter/CLI)
from manage_books import add_book, view_books
from borrow_return import borrow_book, return_book

def main_menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ")
            print(f"DEBUG: User selected choice {choice}")  # Debugging line

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                category = input("Enter book category: ")
                available = int(input("Enter number of copies: "))
                add_book(title, author, category, available)

            elif choice == "2":
                view_books()

            elif choice == "3":
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                borrow_book(user_id, book_id)

            elif choice == "4":
                transaction_id = int(input("Enter transaction ID: "))
                return_book(transaction_id)

            elif choice == "5":
                print("Exiting system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")  # Error handling for unexpected inputs

main_menu()
