
from utilities.file_manager import FileManager
from utilities.classes.book_class import Book

if __name__ == "__main__":

    new_file = FileManager("resources/test.txt")

    new_file.open()

    new_book = Book(123456789, "How to cry alone", "My Sunbathed Balls", "comedy")

    new_file.create()

    new_file.create()

    new_book_2 = Book(136475869, "From Corporal to Dick", "Mary's Little Goat", "drama")
