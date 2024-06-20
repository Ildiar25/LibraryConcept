
from utilities.log_config import *
from utilities.file_manager import FileManager
from utilities.classes.book_class import Book
from utilities.classes.client_class import Client
from utilities.utl import BOOKS_FILE, CLIENTS_FILE

import colorama

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Library:

    def __init__(self):
        """
        This builder creates a library-type object to control two lists.
        One of them will contain a Book list and the other one will contain a Client list.
        """
        self.book_list: list[Book] = []
        self.client_list: list[Client] = []
        logger.info(f"New Library-type object created!")
        logger.debug(f"CONTENT: {self.__dict__}")

    # Main methods
    def load_books(self) -> None:
        """
        This function allows to load content from a file to our book list.
        :return: None
        """
        main_file = FileManager(f"resources/{BOOKS_FILE}")
        book_list = main_file.open()

        if book_list is None or len(book_list) == 0:
            print(" · ¡No hay datos almacenados en Libros!")

        else:
            for element in book_list:
                try:
                    isbn = int(element[0])  # We need to cast this value to integer!
                    title = element[1]
                    author = element[2]
                    genre = element[3]
                    status = element[4]

                except IndexError as err:
                    logger.warning(err)
                    print(f"\n[{type(err).__name__}]#### ¡Parece que algunos datos en '{BOOKS_FILE}' se han perdido!")

                else:
                    book = Book(isbn, title, author, genre, status)
                    self.book_list.append(book)
                    logger.info(f"'{book.title}' added to Book list.")

            # I don't understand why Pycharm says 'unresolved attribute reference isbn for class list',
            # it works as it should do and doesn't raise any error. It is written on the file too and works perfectly.
            logger.debug(f"BOOK LIST UPDATE: {[b_isbn.isbn for b_isbn in self.book_list]}")
            print(" · ¡Libros cargados!")

    def load_clients(self) -> None:
        """
        This function allows to load content from a file to our client list.
        :return: None
        """
        main_file = FileManager(f"resources/{CLIENTS_FILE}")
        client_list = main_file.open()

        if client_list is None or len(client_list) == 0:
            print(" · ¡No hay datos almacenados en Clientes!")

        else:
            for element in client_list:
                try:
                    ident = element[0]
                    name = element[1]
                    surname = element[2]
                    max_allowed = int(element[3])  # We need to cast this value to integer!
                    book_data = element[4]  # That's a string representation of a string!

                except IndexError as err:
                    logger.warning(err)
                    print(f"\n[{type(err).__name__}]#### ¡Parece que algunos datos en '{CLIENTS_FILE}' se han perdido!")

                else:
                    # We need to erase the simbols and cast string numbers into integers
                    list_str: list[str] = book_data.strip("][").split(", ")
                    isbn_list: list[int] = []

                    for number in list_str:
                        if number.isdigit():
                            number = int(number)
                            isbn_list.append(number)

                    client = Client(ident, name, surname, max_allowed, isbn_list)
                    self.client_list.append(client)
                    logger.info(f"'{client.name}' added to Client list.")

            # I don't understand why Pycharm says 'unresolved attribute reference ident for class list',
            # it works as it should do and doesn't raise any error. It is written on the file too and works perfectly.
            logger.debug(f"CLIENT LIST UPDATE: {[c_id.ident for c_id in self.client_list]}")
            print(" · ¡Clientes cargados!")

    def save_books(self) -> None:
        """
        This function allows to prepare data to be written.
        :return: None
        """
        main_file = FileManager(f"resources/{BOOKS_FILE}")
        ready_books: list[tuple] = []

        for book in self.book_list:
            data = (book.isbn, book.title, book.author, book.genre, book.status)
            ready_books.append(data)

        logger.debug(f"{ready_books=}")
        main_file.save(ready_books)

    def save_clients(self) -> None:
        """
        This function allows to prepare data to be written.
        :return: None
        """
        main_file = FileManager(f"resources/{CLIENTS_FILE}")
        ready_clients: list[tuple] = []

        for client in self.client_list:
            data = (client.ident, client.name, client.surname, client.max_allowed, client.book_list)
            ready_clients.append(data)

        logger.debug(f"{ready_clients=}")
        main_file.save(ready_clients)

    def add_book(self, isbn, title, author, genre) -> None:
        """
        This function allows to create a book-type object and append it to book list.
        :param isbn: nine numbers integer
        :param title: name of the book in string format
        :param author: book's author in string format
        :param genre: book's genre in string format
        :return: None
        """
        book = Book(isbn, title, author, genre)
        self.book_list.append(book)
        print("¡Libro añadido!")
        logger.debug(f"Book '{book.title}' added to book list: '{[b_name.title for b_name in self.book_list]}'.")

    def add_client(self, ident, name, surname) -> None:
        """
        This function allows to create a client-type object and append it to client list
        :param ident: alphanumeric code with nine elements
        :param name: client's name in string format
        :param surname: client's surname in string format
        :return:
        """
        client = Client(ident, name, surname)
        self.client_list.append(client)
        print("¡Cliente añadido!")
        logger.debug(f"Client '{client.name}' added to client list: '{[c_name.name for c_name in self.client_list]}'.")

    def look_for_book(self, isbn: int) -> Book:
        """
        This function allows to look for a book by its isbn.
        :param isbn: nine numbers integer
        :return: the book finded
        """
        for book in self.book_list:
            if book.isbn == isbn:
                return book

    def look_for_client(self, ident: str) -> Client:
        """
        This function allows to look for a client by his ident number.
        :param ident: alphanumeric code with nine elements
        :return: the client finded
        """
        for client in self.client_list:
            if client.ident == ident:
                return client

    def show_books(self):

        for book in self.book_list:

            # Create text format
            format_isbn = " {:^10}".format(str(book.isbn)[:10])
            format_title = " {:<85}".format(book.title[:85].upper())
            format_author = " {:<20}".format(book.author[:20].upper())
            format_genre = " {:<10}".format(book.genre[:10].upper())
            format_status = " {:^12}".format(book.status[:12].upper())

            # Prepare colors
            available = colorama.Fore.GREEN
            reserved = colorama.Fore.YELLOW
            unavailable = colorama.Fore.RED
            reset = colorama.Fore.RESET

            # Add conditionals
            if book.status == "disponible":
                print(f"||{format_isbn}|{format_title}|{format_author}|{format_genre}|{available}"
                      f"{format_status}{reset}||")
            elif book.status == "reservado":
                print(f"||{format_isbn}|{format_title}|{format_author}|{format_genre}|{reserved}"
                      f"{format_status}{reset}||")
            elif book.status == "prestado":
                print(f"||{format_isbn}|{format_title}|{format_author}|{format_genre}|{unavailable}"
                      f"{format_status}{reset}||")

    def show_clients(self):

        for client in self.client_list:

            # Prepare client book list
            book_list = " | ".join([str(isbn) for isbn in client.book_list])

            # Create text format
            format_ident = "  {:^10} ".format(client.ident)
            format_name = " {:<79} ".format(client.name.upper() + " " + client.surname.upper())
            format_books = "  [{:^38}]  ".format(book_list)
            format_quantity = "{:^5}".format(str(client.max_allowed - len(client.book_list)))

            # Prepare colors
            available = colorama.Fore.GREEN
            adviced = colorama.Fore.YELLOW
            unavailable = colorama.Fore.RED
            reset = colorama.Fore.RESET

            # Add conditionals
            if len(client.book_list) == 3:
                print(f"||{format_ident}|{format_name}|{format_books}|{unavailable}{format_quantity}{reset}||")
            elif len(client.book_list) == 2:
                print(f"||{format_ident}|{format_name}|{format_books}|{adviced}{format_quantity}{reset}||")
            elif len(client.book_list) == 1:
                print(f"||{format_ident}|{format_name}|{format_books}|{adviced}{format_quantity}{reset}||")
            elif len(client.book_list) == 0:
                print(f"||{format_ident}|{format_name}|{format_books}|{available}{format_quantity}{reset}||")
