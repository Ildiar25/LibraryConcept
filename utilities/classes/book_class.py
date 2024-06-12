
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
        logger.info("New object-book type created")

    # Main methods
    def lend_book(self) -> None:
        pass

    def return_book(self) -> None:
        pass

    def save_book(self) -> None:
        pass
