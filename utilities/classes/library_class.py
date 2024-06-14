
from utilities.log_config import *
from utilities.file_manager import FileManager
from utilities.classes.book_class import Book
from utilities.classes.client_class import Client

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Library:

    def __init__(self):

        self.book_list: list[Book] = []
        self.client_list: list[Client] = []
        logger.debug("New Library-type object created.")

    # Main methods
    def load_books(self) -> None:

        main_file = FileManager("resources/books.csv")
        book_list = main_file.open()

        if book_list is None:
            print("No hay datos almacenados!")

        else:
            for element in book_list:
                try:
                    isbn = element[0]
                    name = element[1]
                    author = element[2]
                    genre = element[3]
                    status = element[4]

                except IndexError as err:
                    print("\nNo se puede cargar el archivo.")
                    logger.error(err)
                    break  # I am not sure about what I am doing here, really.

                else:
                    book = Book(isbn, name, author, genre, status)
                    self.book_list.append(book)

    def load_clients(self) -> None:

        main_file = FileManager("resources/clients.csv")
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
                    book_data = element[4]

                except IndexError as err:
                    print("\nNo se puede cargar el archivo.")
                    logger.error(err)
                    break

                else:

                    client = Client(ident, name, surname, max_allowed)
                    self.client_list.append(client)

    def save_books(self) -> None:
        pass

    def save_clients(self) -> None:
        pass

    def add_book(self) -> None:
        pass

    def add_client(self) -> None:
        pass
