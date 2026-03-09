#библиотеке
import sqlite3
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str = "available"

@dataclass
class Reader:
    id: int
    name: str
    age: int

class Library:
    def __init__(self, db_name = "library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year INTEGER,
            status TEXT CHECK (status IN ("available", "borrowed")) DEFAULT "available"
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowed_books (
            reader_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT,
            FOREIGN KEY(reader_id) REFERENCES readers(id),
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
        """)

        self.conn.commit()


def add_book(self):
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = int(input("Введите год издания: "))
    self.cursor.execute(""" 
    INSERT INTO borrowed_books (reader_id, book_id, borrow_date)
    VALUES (?, ?, ?)
    """, (title, author, year)) #выдача
    self.conn.commit()
    print("книга добавлена")

def add_reader(self):
    name = input("Введите имя читателя: ")
    age = int(input("Введите возраст: "))
    self.cursor.execute("""
    INSERT INTO readers (name, age)
    VALUES (?, ?)
    """, (name, age))
    self.conn.commit()
    print("читатель добавлен!")

def borrow_book(self):
    reader_id = int(input("Введите ID читателя: "))
    book_id = int(input("Введите ID книги: "))
    self.cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
    result = self.cursor.fetchone()
    if result and result[0] == "available":
       borrow_date = datetime.now().strftime("%Y-%m-%d")
       self.cursor.execute("""
       INSERT INTO borrowed_books (reader_id, book_id, borrow_date)
       VALUES (?, ?, ?)
       """, (reader_id, book_id, borrow_date))
       self.cursor.execute("""
       UPDATE books
       SET status = 'borrowed'
       WHERE id = ?
       """, (book_id,))
       self.conn.commit()
       print("книга выдана!")
    else:
       print("книга уже занята или не существует")

def return_book(self):
    book_id = int(input("Введите ID книги для возврата: "))

    self.cursor.execute("""
    DELETE FROM borrowed_books
    WHERE book_id = ?
    """, (book_id,))
    self.cursor.execute("""
    UPDATE books
    SET status = 'available'
    WHERE id = ?
    """, (book_id,))
    self.conn.commit()
    print("книга возвращена")

def search_books(self):
    keyword = input("Введите слово для поиска: ")
    self.cursor.execute("""
    SELECT * FROM books
    WHERE title LIKE ? OR author LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    results = self.cursor.fetchall()
    if results:
        print("\nнайденные книги:")
        for book in results:
            print(book)
    else:
        print("ничего не найдено")

def show_borrowed_books(self):
    self.cursor.execute("""
            SELECT readers.name, books.title, borrowed_books.borrow_date
            FROM borrowed_books
            JOIN readers ON borrowed_books.reader_id = readers.id
            JOIN books ON borrowed_books.book_id = books.id
            """)
    results = self.cursor.fetchall()
    if results:
        print("\nвыданные книги:")
        for row in results:
            print(f"Читатель: {row[0]}, Книга: {row[1]}, Дата: {row[2]}")
    else:
        print("нет выданных книг")

def get_statistics(self):
    self.cursor.execute("""
            SELECT status, COUNT(*)
            FROM books
            GROUP BY status
            """)
    stats = self.cursor.fetchall()
    print("\nСтатистика:")
    for status, count in stats:
        print(f"{status}: {count}")

def close(self):
    self.conn.close()