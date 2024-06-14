
from utilities.log_config import *
from utilities.classes.book_class import Book

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Client:

    def __init__(self, ident: int, name: str, surname: str, max_allowed: int = 3, book_list: list[Book] = None):
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
        logger.debug(f"New client-type object created: '{self.name.upper()}'")

    def take_away(self, isbn: int, main_book_list: list[Book]) -> None:

        for book in main_book_list:
            if book.isbn == isbn:
                if len(self.book_list) < self.max_allowed and book.status == "disponible":
                    self.book_list.append(book)
                    logger.info(f"Book '{book.title}' added to {self.name}'s list")
                    book.lent(self.name.capitalize())

                else:
                    print("\nNo se puede llevar este ejemplar. Tiene el cupo completo o no se encuentra disponible.")
                    logger.debug(f"Client list: {[b_name.title for b_name in self.book_list]} | {book.title.upper()} "
                                 f"status:'{book.status}'")

    def give_back(self, isbn: int, main_book_list: list[Book]) -> None:

        for index in range(len(self.book_list)):
            if isbn == self.book_list[index].isbn:
                got_book = self.book_list.pop(index)
                logger.info(f"'{got_book.title.capitalize()}' erased from {self.name.capitalize()}'s list")
                logger.debug(f"User's books: '{[name.title for name in self.book_list]}'")

                for book in main_book_list:
                    if book.isbn == isbn:
                        book.returned(self.name.capitalize())
                        logger.info(f"The book '{book.title}' has change its status to '{book.status}'.")

    def save_book(self, isbn: int, main_book_list: list[Book]) -> None:

        for book in main_book_list:
            if book.isbn == isbn:
                if book.status == "prestado":
                    book.saved(self.name.capitalize())
                    logger.info(f"'{book.title}' reserved by '{self.name}'")

                else:
                    print(f"El libro '{book.title.capitalize()}' se encuentra {book.status}.")
