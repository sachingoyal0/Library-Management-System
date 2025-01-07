# Code for managing books
# 2. manage_books.py
from db_connection import get_connection

def add_book(title, author, category, available):
    """Add a new book to the library."""
    try:
        conn = get_connection()
        if not conn:
            raise Exception("Database connection failed")

        cursor = conn.cursor()
        query = """
            INSERT INTO books (title, author, category, available) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (title, author, category, available))
        conn.commit()
        print("Book added successfully!")
    except Exception as e:
        print(f"Error in add_book: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()


def view_books():
    """View all books in the library."""
    try:
        conn = get_connection()
        if not conn:
            raise Exception("Database connection failed")

        cursor = conn.cursor()
        query = "SELECT * FROM books"
        cursor.execute(query)
        books = cursor.fetchall()

        if not books:
            print("No books found in the library.")
            return

        # Dynamic column display using cursor.description
        column_names = [desc[0] for desc in cursor.description]
        print("\n--- Available Books ---")
        print(" | ".join(column_names))
        print("-" * (len(column_names) * 15))
        for book in books:
            print(" | ".join(map(str, book)))
    except Exception as e:
        print(f"Error in view_books: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()


def borrow_book(user_id, book_id):
    """Record a book borrowing transaction."""
    try:
        conn = get_connection()
        if not conn:
            raise Exception("Database connection failed")

        cursor = conn.cursor()

        # Check availability
        check_query = "SELECT available FROM books WHERE book_id = %s"
        cursor.execute(check_query, (book_id,))
        result = cursor.fetchone()
        if not result:
            print("Book ID not found!")
            return
        if result[0] <= 0:
            print("Book is not available!")
            return

        # Borrow book
        query = """
            INSERT INTO transactions (user_id, book_id, borrow_date) 
            VALUES (%s, %s, CURDATE())
        """
        cursor.execute(query, (user_id, book_id))
        update_query = """
            UPDATE books 
            SET available = available - 1 
            WHERE book_id = %s
        """
        cursor.execute(update_query, (book_id,))
        conn.commit()
        print("Book borrowed successfully!")
    except Exception as e:
        if conn and conn.is_connected():
            conn.rollback()  # Rollback transaction if error occurs
        print(f"Error in borrow_book: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
