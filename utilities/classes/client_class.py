
from utilities.log_config import *
from utilities.classes.book_class import Book

# Create our logger from Book to work with
logger = logging.getLogger(__name__)


class Client:

    def __init__(self, ident: int, name: str, surname: str, max_allowed: int):
        self.ident = ident
        self.name = name
        self.surname = surname
        self.max_allowed = max_allowed
        self.book_list: list[Book] = []
