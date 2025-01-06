"SQL script to create the database and tables"
-- Create Database
CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

-- Create Books Table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    available INT NOT NULL CHECK (available >= 0) -- Ensures non-negative values
);

-- Create Users Table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE, -- Ensures unique emails
    phone VARCHAR(15) UNIQUE -- Ensures unique phone numbers
);

-- Create Transactions Table
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL DEFAULT CURDATE(),
    return_date DATE DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Add Indexes for Faster Queries
CREATE INDEX idx_user_id ON transactions (user_id);
CREATE INDEX idx_book_id ON transactions (book_id);

-- Additional Indexes for Books (Optional)
CREATE INDEX idx_title ON books (title);
CREATE INDEX idx_author ON books (author);
CREATE INDEX idx_category ON books (category);
