
from utilities.log_config import *
from utilities.file_manager import FileManager
from utilities.classes.book_class import Book
from utilities.classes.client_class import Client
from utilities.utl import BOOKS_FILE, CLIENTS_FILE

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Library:

    def __init__(self):

        self.book_list: list[Book] = []
        self.client_list: list[Client] = []
        logger.debug("New Library-type object created.")

    # Main methods
    def load_books(self) -> None:

        main_file = FileManager(f"resources/{BOOKS_FILE}")
        book_list = main_file.open()

        if book_list is None:
            print("No hay datos almacenados!")

        else:
            for element in book_list:
                try:
                    isbn = element[0]
                    title = element[1]
                    author = element[2]
                    genre = element[3]
                    status = element[4]

                except IndexError as err:
                    print("\nNo se puede cargar el archivo.")
                    logger.error(err)
                    break  # I am not sure about what I am doing here, really.

                else:
                    book = Book(isbn, title, author, genre, status)
                    self.book_list.append(book)

    def load_clients(self) -> None:

        main_file = FileManager(f"resources/{CLIENTS_FILE}")
        client_list = main_file.open()

        if client_list is None:
            print("No hay datos almacenados!")

        else:
            for element in client_list:
                try:
                    ident = element[0]
                    name = element[1]
                    surname = element[2]
                    max_allowed = element[3]
                    book_data = element[4]  # That's a string representation of a string!

                except IndexError as err:
                    print("\nNo se puede cargar el archivo.")
                    logger.error(err)
                    break  # I am not sure about what I am doing here, really.

                else:
                    # We need to erase the simbols and cast string numbers into integers
                    list_str: list[str] = book_data.strip("[]").split(", ")
                    isbn_list: list[int] = []

                    for number in list_str:
                        if number.isdigit():
                            number = int(number)
                            isbn_list.append(number)

                    client = Client(ident, name, surname, max_allowed, isbn_list)
                    self.client_list.append(client)

    def save_books(self) -> None:

        main_file = FileManager(f"resources/{BOOKS_FILE}")
        ready_books: list[tuple] = []

        for book in self.book_list:
            data = (book.isbn, book.title, book.author, book.genre, book.status)
            ready_books.append(data)

        main_file.save(ready_books)
        logger.info(f"Data saved correctly into '{BOOKS_FILE}'!")

    def save_clients(self) -> None:

        main_file = FileManager(f"resources/{CLIENTS_FILE}")
        ready_clients: list[tuple] = []

        for client in self.client_list:
            data = (client.ident, client.name, client.surname, client.max_allowed, client.book_list)
            ready_clients.append(data)

        main_file.save(ready_clients)
        logger.info(f"Data saved correctly into '{CLIENTS_FILE}'!")

    def add_book(self, isbn, title, author, genre) -> None:

        book = Book(isbn, title, author, genre)
        self.book_list.append(book)

    def add_client(self, ident, name, surname) -> None:

        client = Client(ident, name, surname)
        self.client_list.append(client)
