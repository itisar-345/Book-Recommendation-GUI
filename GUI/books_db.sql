-- Run this file using MySQL Client or Command Line

-- Create the database
CREATE DATABASE IF NOT EXISTS book;

-- Use the created database
USE book;

-- Create the `books` table
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    author VARCHAR(255),
    description TEXT,
    genres VARCHAR(255),
    goodreads_rating FLOAT,
    amazon_rating FLOAT,
    bookish_rating FLOAT,
    fantastic_fiction_rating FLOAT,
    book_depository_rating FLOAT
);

-- Insert records into the `books` table
INSERT INTO books (title, author, genres, description, goodreads_rating, amazon_rating, bookish_rating, fantastic_fiction_rating, book_depository_rating)
VALUES
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 'A classic novel that explores racial injustice and moral growth in the American South during the 1930s.', 4.28, 4.7, 4.2, 4.1, 4.5),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic, Fiction', 'Set in the Roaring Twenties, this novel explores the decadence and excess of the Jazz Age in America.', 3.91, 4.3, 4.0, 3.8, 4.2),
('1984', 'George Orwell', 'Dystopian, Fiction', 'A chilling vision of a totalitarian regime and the dangers of absolute power.', 4.18, 4.6, 4.4, 4.3, 4.5),
('Pride and Prejudice', 'Jane Austen', 'Classic, Romance', 'A witty exploration of love, social class, and self-discovery.', 4.26, 4.8, 4.5, 4.2, 4.6),
('The Catcher in the Rye', 'J.D. Salinger', 'Classic, Fiction', 'A coming-of-age story about teenage angst and rebellion.', 3.81, 4.1, 3.9, 3.8, 4.0),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy, Adventure', 'A prelude to The Lord of the Rings, exploring Bilbo Baggins\' unexpected journey.', 4.27, 4.8, 4.6, 4.5, 4.7),
('The Alchemist', 'Paulo Coelho', 'Philosophy, Adventure', 'A philosophical tale of a shepherd seeking his personal legend.', 3.88, 4.5, 4.3, 4.1, 4.4),
('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'Fantasy, Young Adult', 'The magical journey of a young wizard discovering his destiny.', 4.47, 4.9, 4.8, 4.6, 4.7),
('The Kite Runner', 'Khaled Hosseini', 'Fiction, Drama', 'A gripping tale of friendship, betrayal, and redemption.', 4.34, 4.7, 4.5, 4.3, 4.6),
('The Da Vinci Code', 'Dan Brown', 'Thriller, Mystery', 'A fast-paced thriller exploring art, religion, and historical secrets.', 3.89, 4.4, 4.2, 4.1, 4.3);