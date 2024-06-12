
from utilities.file_manager import FileManager
from utilities.classes.book_class import Book

if __name__ == "__main__":

    new_file = FileManager("resources/test.txt")

    new_file.open()

    new_book = Book(123456789, "How to cry alone", "My Sunbathed Balls", "comedy")
    new_book_2 = Book(136475869, "From Corporal to Dick", "Mary's Little Goat", "drama")

    print(f"\nNuevo libro: {new_book.title}")
    print("Estado:", new_book.status)
    new_book.lend_book("Joan")

    print("\nEstado actual:", new_book.status)

    new_file.create()

    print("Nuevo cliente María:")
    print(f"Quiere {new_book.title}:")
    new_book.lend_book("Maria")

    new_book_2.return_book("Maria")

    new_file.create()
