
from utilities.log_config import *
from utilities.classes.book_class import Book

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Client:

    def __init__(self, ident: str, name: str, surname: str, max_allowed: int = 3, book_list: list[int] = None):
        """
        This builder creates a client-type object to save its representative data
        :param ident: Alphanumeric code with nine elements
        :param name: client's name in string format
        :param surname: client's surname in string format
        :param max_allowed: max quantity of books in integer ('3' by default)
        """
        self.ident = ident
        self.name = name
        self.surname = surname
        self.max_allowed = max_allowed

        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list

        logger.info(f"New Client-type object as '{self.name.capitalize()}' created!")

    def take_away(self, book: Book) -> None:
        """
        This function allows to change the status-object according to different statements.
        :param book: a book-type object to interact with
        :return: None
        """
        if len(self.book_list) < self.max_allowed and book.status == "disponible":
            logger.debug(f"Actual ISBN list: {[number for number in self.book_list]} ## New ISBN: {book.isbn}")
            self.book_list.append(book.isbn)
            book.lent()

            logger.debug(f"Client list updated: {[number for number in self.book_list]}")

        else:
            print("\nNo se puede llevar ningún ejemplar hasta que devuelva los que ya posee.")

    def give_back(self, book: Book) -> None:
        """
        This function allows to change the status-object according to different statements.
        :param book: a book-type object to interact with
        :return:
        """
        if book.isbn in self.book_list:
            logger.debug(f"Actual ISBN list: {[number for number in self.book_list]} ## ISBN erased: {book.isbn}")
            self.book_list.remove(book.isbn)
            book.returned()

            logger.debug(f"Client list updated: {[number for number in self.book_list]}")

        else:
            print("No dispone de ese libro en su cuenta.")

    def save_book(self, book: Book) -> None:
        """
        This function allows to change the status-object according to different statements
        :param book: a book-type object to interact with
        :return: None
        """
        if book.isbn not in self.book_list and book.status == "prestado":
            logger.debug(f"Actual ISBN list: {[number for number in self.book_list]} ## ISBN saved: {book.isbn}")
            book.saved()

            logger.debug(f"Actual book status: '{book.status}'.")

        else:
            print("Ya dispone de ese ejemplar.")
