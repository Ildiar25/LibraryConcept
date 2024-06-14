
from utilities.file_manager import FileManager
from utilities.log_config import *

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Book:

    def __init__(self, isbn: int, title: str, author: str, genre: str, status: str = "disponible") -> None:
        """
        This builder creates a book-type object to save its representative data
        :param isbn: nine numbers integer
        :param title: name of the book in string format
        :param author: book's author in string format
        :param genre: book's genre in string format
        :param status: three string choices: ['disponible', 'prestado', 'reservado'], 'disponible' by default
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        logger.debug(f"New book-type object created: '{self.title}'")

    # Main methods
    def lent(self, user_name: str) -> None:
        self.status = "prestado"
        print(f"\nEl libro ha sido prestado a {user_name}.")
        logger.info(f"Book '{self.title}' lended to '{user_name}'.")

    def returned(self, user_name: str) -> None:
        self.status = "disponible"
        print(f"El libro ha sido devuelto por '{user_name}'.")
        logger.info(f"Book '{self.title}' given back by '{user_name}'.")

    def saved(self, user_name: str) -> None:
        self.status = "reservado"
        print(f"El libro ha sido reservado por {user_name}")
        logger.info(f"Book '{self.title}' saved by '{user_name}'.")
