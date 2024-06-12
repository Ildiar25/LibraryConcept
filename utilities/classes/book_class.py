
from utilities.file_manager import FileManager
from utilities.log_config import *

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Book:

    def __init__(self, isbn: int, title: str, author: str, genre: str, status: str = "disponible") -> None:
        """
        This builder creates a book-type object to save its representative data
        :param isbn:
        :param title:
        :param author:
        :param genre:
        :param status:
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        logger.debug(f"New book-type object created: '{self.title}'")

    # Main methods
    def lend_book(self, user_name: str) -> None:

        if self.status == "disponible":
            self.status = "prestado"
            print(f"\nEl libro ha sido prestado a {user_name}.")
            logger.info(f"Book '{self.title}' lended to '{user_name}'.")

        else:
            print(f"Lo siento, el libro que ha pedido se encuentra {self.status}.")

    def return_book(self, user_name: str) -> None:

        if self.status == "prestado" or self.status == "reservado":
            self.status = "disponible"
            print(f"El libro ha sido devuelto por '{user_name}'.")
            logger.info(f"Book '{self.title}' given back by '{user_name}'.")

        else:
            print(f"Lo siento, el libro que ha pedido ya se encuentra {self.status}.")

    def save_book(self, user_name: str) -> None:

        if self.status == "prestado":
            self.status = "reservado"
            print(f"El libro ha sido reservado por {user_name}")
            logger.info(f"Book '{self.title}' saved by '{user_name}'.")

        else:
            print(f"Lo siento, no se puede reservar un libro que ya se encuentra {self.status}.")
