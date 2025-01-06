# Code for borrow and return functionality
# 3. borrow_return.py
from db_connection import get_connection

def close_connection(conn):
    """Helper to close the database connection."""
    if conn and conn.is_connected():
        conn.close()

def borrow_book(user_id, book_id):
    """Record a book borrowing transaction."""
    try:
        conn = get_connection()
        if not conn:
            raise Exception("Database connection failed")

        cursor = conn.cursor()

        # Check book availability
        check_query = "SELECT available FROM books WHERE book_id = %s"
        cursor.execute(check_query, (book_id,))
        result = cursor.fetchone()
        if not result:
            print("Book not found in the library!")
            return
        if result[0] <= 0:
            print("Book is not available!")
            return

        # Borrow book
        borrow_query = "INSERT INTO transactions (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())"
        cursor.execute(borrow_query, (user_id, book_id))
        update_query = "UPDATE books SET available = available - 1 WHERE book_id = %s"
        cursor.execute(update_query, (book_id,))

        conn.commit()
        print("Book borrowed successfully!")
    except Exception as e:
        print(f"Error in borrow_book: {e}")
    finally:
        close_connection(conn)

def return_book(transaction_id):
    """Record a book return transaction."""
    try:
        conn = get_connection()
        if not conn:
            raise Exception("Database connection failed")

        cursor = conn.cursor()

        # Start transaction
        conn.start_transaction()

        # Check if the transaction exists and hasn't been returned yet
        check_query = "SELECT book_id FROM transactions WHERE transaction_id = %s AND return_date IS NULL"
        cursor.execute(check_query, (transaction_id,))
        result = cursor.fetchone()
        if not result:
            print("Invalid transaction ID or book already returned!")
            conn.rollback()
            return

        book_id = result[0]

        # Update transaction and increment book availability
        update_transaction_query = "UPDATE transactions SET return_date = CURDATE() WHERE transaction_id = %s"
        cursor.execute(update_transaction_query, (transaction_id,))
        update_book_query = "UPDATE books SET available = available + 1 WHERE book_id = %s"
        cursor.execute(update_book_query, (book_id,))

        conn.commit()
        print("Book returned successfully!")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error in return_book: {e}")
    finally:
        close_connection(conn)
