import random
from enum import Enum


class Library:
    books = []

    def __init__(self):
        self.books.append(Book("Harry - I"))
        self.books.append(Book("Harry - II", Status.NOT_AVAILABLE, "Anton"))
        self.books.append(Book("Harry - III"))
        self.books.append(Book("Harry - IV", Status.NOT_AVAILABLE, "Anton"))
        self.books.append(Book("Harry - V", Status.NOT_AVAILABLE, "Anton"))
        self.books.append(Book("Harry - VI"))

    def display(self):
        available_book = 0
        total_book = len(self.books)
        for book in self.books:
            if book.STATUS == Status.AVAILABLE:
                print(f"Available Book, #{available_book}  -| '{book.NAME}'")
                available_book += 1
        print(f"Overall there are: {total_book} Books, {total_book - available_book} of them borrowed.\n")

    def add_books(self):
        book_name = input(
            "Which book do you want to add to our library? \n ")
        book = Book(book_name)
        if book.is_name_valid():
            self.books.append(book)
        else:
            print("Invalid book name, returning to the Menu.")
            self.display_menu()

    def borrow(self):
        username = input("Welcome to our Library!\n What's your Username?\n ")
        book_name = input("What book do you want to borrow?\n ")
        book = self.find_book_by_name(book_name, Status.AVAILABLE)
        if book is not None:
            book.STATUS = Status.NOT_AVAILABLE
            book.OWNER = username
            print('You have successfully borrowed a book!')
        else:
            print('Sorry, the book is not available for borrowing.')

    def display_user_books(self):
        username = input("What's your Username?\n ")
        user_books = self.find_books_by_username(username)

        for index, book in enumerate(user_books, start=1):
            print(f"Book #{index}  -| '{book.NAME}'")
        print(f"Overall you have: {len(user_books)} Book(s)\n")

    def return_user_book(self):
        username = input("What's your Username?\n ")
        book_name = input("What book do you want to return?\n ")
        book = self.find_book_by_name_and_username(book_name, username, Status.NOT_AVAILABLE)
        if book is None:
            print('Sorry, you have not borrowed this book or it does not exist in our records.')
        else:
            book.STATUS = Status.AVAILABLE
            book.OWNER = "Library"
            print('You have successfully returned a book!')

    def find_book_by_name(self, name, status):
        for book in self.books:
            if name == book.NAME and book.STATUS == status:
                return book

    def find_book_by_name_and_username(self, name, username, status):
        for book in self.books:
            if name == book.NAME and username == book.OWNER and book.STATUS == status:
                return book

    def find_books_by_username(self, username):
        book_list = []
        for book in self.books:
            if username == book.OWNER:
                book_list.append(book)
        return book_list

    def display_menu(self):
        while True:
            choice = input(
                "Display Available Books - 1\nBorrow a book - 2\nReturn a book - 3\nView your books - 4\nAdd your "
                "book - 5\nExit the script - 6\n\nEnter your choice [1-6]: ")
            if choice == '1':
                self.display()
            elif choice == '2':
                self.borrow()
            elif choice == '3':
                self.return_user_book()
            elif choice == '4':
                self.display_user_books()
            elif choice == '5':
                self.add_books()
            elif choice == '6':
                print("Exiting script, Bye.")
                break


class Status(Enum):
    AVAILABLE = 0
    NOT_AVAILABLE = 1


class Book:
    def __init__(self, name, status=Status.AVAILABLE, owner="Library"):
        self.ID = generate_id()
        self.NAME = name
        self.STATUS = status
        self.OWNER = owner

    def is_name_valid(self):
        if self.NAME == "" or self.NAME == " ":
            return False
        else:
            return True


def generate_id():
    random_part = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    numeric_part = ''.join(random.choices('0123456789', k=6))
    new_id = f"{numeric_part}-{random_part}"
    return new_id


Library().display_menu()
