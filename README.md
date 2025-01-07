# Library Management System

A **Library Management System** built with Python that allows users to manage book inventories, track borrowing and returning of books, and handle transactions efficiently. This project is ideal for educational purposes or as a starting point for real-world implementations.

---

## Features

- **Add Books:** Add new books to the library database with details such as title, author, category, and availability.
- **View Books:** View all available books in the library with their details.
- **Borrow Books:** Borrow books and automatically update their availability in the database.
- **Return Books:** Return borrowed books, which updates the transaction records and restores availability.
- **Transaction Tracking:** Maintains a history of all borrow and return transactions for each user.

---

## Technologies Used

- **Backend:** Python
- **Database:** MySQL (Local or Cloud-based with Heroku integration)
- **Version Control:** Git and GitHub
- **Optional UI:** Command-line interface (CLI) for basic interaction

---

## Prerequisites

Ensure you have the following installed on your system:

1. Python (>=3.7)
2. MySQL Server
3. pip (Python package manager)
4. Git

---

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/<your-username>/Library-Management-System.git
   cd Library-Management-System
   ```

2. **Set Up the Database**

   - Use the provided SQL script (`database_setup.sql`) to create the required database and tables.
   - Execute the script using MySQL Workbench or the MySQL CLI.

   ```sql
   source path_to_sql_file/database_setup.sql;
   ```

3. **Configure Database Connection**

   - Update `db_connection.py` with your database credentials:
     ```python
     config = {
         'user': 'your_username',
         'password': 'your_password',
         'host': 'localhost',
         'database': 'LibraryDB',
     }
     ```

4. **Install Dependencies** (if required):

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**

   Execute the main script to start the CLI interface:
   ```bash
   python ui_main.py
   ```

---

## Usage Instructions

### Add a Book
Follow the prompts to add a book by entering the title, author, category, and the number of available copies.

### View Books
View the list of all books along with their availability status.

### Borrow a Book
Provide the user ID and book ID to borrow a book. The availability will decrease by 1.

### Return a Book
Provide the transaction ID to return a book. The availability will increase by 1.

---

## Deployment on Heroku (Optional)

To make your application accessible online:

1. Set up a free Heroku account and create an app.
2. Use the Heroku PostgreSQL add-on for database hosting.
3. Update your database credentials in `db_connection.py` to point to the Heroku database.
4. Deploy your code to Heroku by connecting it to your GitHub repository.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this project as per the license terms.

---

## Contact

For any queries or suggestions, feel free to contact:

- **Name:** Sachin Goyal
- **Email:** your_email@example.com
- **GitHub:** [sachingoyal0](https://github.com/sachingoyal0)

