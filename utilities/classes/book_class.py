
#

from utilities.log_config import *

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Book:

    def __init__(self, isbn: int, title: str, author: str, genre: str, status: str = "disponible") -> None:
        """
        This builder creates a book-type object to save its representative data.
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
        logger.info(f"New Book-type object created!")
        logger.debug(f"CONTENT: {self.__dict__}")

    # Main methods
    def lent(self) -> None:
        """
        This function changes 'self.status' to another one.
        :return: None
        """
        self.status = "prestado"
        logger.debug(f"{self.status=} for book '{self.title}'")
        print(f"¡Libro prestado!")

    def returned(self) -> None:
        """
        This function changes 'self.status' to another one.
        :return: None
        """
        self.status = "disponible"
        logger.debug(f"{self.status=} for book '{self.title}'")
        print(f"¡Libro devuelto!")

    def saved(self) -> None:
        """
        This function changes 'self.status' to another one.
        :return: None
        """
        self.status = "reservado"
        logger.debug(f"{self.status=} for book '{self.title}'")
        print(f"¡Reserva confirmada!")
