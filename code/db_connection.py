# Database connection setup
# Library Management System - Refactored Code

# 1. db_connection.py
# db_connection.py
import mysql.connector
import os

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),  # Ensure correct hostname
            user=os.getenv("DB_USER", "your_mysql_user"),  # Replace with your MySQL username
            password=os.getenv("DB_PASS", "your_mysql_pass"),  # Replace with your MySQL password
            database=os.getenv("DB_NAME", "LibraryDB")  # Replace with your database name
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None
    