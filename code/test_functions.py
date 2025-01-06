# Testing the individual functions
# 5. Test cases (test_functions.py)
def test_add_book():
    try:
        add_book("Test Book", "Test Author", "Test Category", 10)
        print("Test add_book passed!")
    except Exception as e:
        print(f"Test add_book failed: {e}")

def test_borrow_book():
    try:
        borrow_book(1, 1)  # Replace with valid user_id and book_id
        print("Test borrow_book passed!")
    except Exception as e:
        print(f"Test borrow_book failed: {e}")

def test_return_book():
    try:
        return_book(1)  # Replace with valid transaction_id
        print("Test return_book passed!")
    except Exception as e:
        print(f"Test return_book failed: {e}")
