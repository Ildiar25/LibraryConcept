
from utilities.file_manager import FileManager
from utilities.classes.book_class import Book
from utilities.classes.client_class import Client

if __name__ == "__main__":

    new_file = FileManager("resources/test.csv")

    new_file.save([(123456789, "How to cry alone", "My sunbathed Balls", "comedy", "disponible"),
                   (246813579, "From Corporal to Dick", "Mary's Little Goat", "drama", "prestado")])
    data_thing = new_file.open()

    print(data_thing)

    new_book = Book(123456789, "How to cry alone", "My Sunbathed Balls", "comedy")
    new_book_2 = Book(246813579, "From Corporal to Dick", "Mary's Little Goat", "drama")

    print("\nLibro 1 diccionario:")
    print(new_book.__dict__)
    print("\nLibro 2 diccionario:")
    print(new_book_2.__dict__)
    #
    # print(f"\nNuevo libro: {new_book.title}")
    # print("Estado:", new_book.status)
    # new_book.lend_book("Joan")
    #
    # print("\nEstado actual:", new_book.status)
    #
    # new_file.create()
    #
    # print("Nuevo cliente María:")
    # print(f"Quiere {new_book.title}:")
    # new_book.lend_book("Maria")
    #
    # new_book_2.return_book("Maria")
    #
    # new_file.create()

    # book_list = [new_book, new_book_2]
    # print("\nPrimera lista:")
    # print(f"{[name.status for name in book_list]}")
    #
    # client_01 = Client(123456789, "Joan", "Pastor")
    # client_02 = Client(246813579, "María", "Gozalbez")
    #
    # client_01.take_away(123456789, book_list)
    #
    # print("\nSegunda lista:")
    # print(f"{[name.status for name in book_list]}")
    #
    # client_02.take_away(246813579, book_list)
    #
    # print("\nTercera lista:")
    # print(f"{[name.status for name in book_list]}")
    #
    # print("\nClient lists:")
    # print(client_01.name, [name.title for name in client_01.book_list])
    # print(client_02.name, [name.title for name in client_02.book_list])
    #
    # client_02.take_away(123456789, book_list)
    # client_01.give_back(123456789, book_list)
    # print(f"{[name.status for name in book_list]}")
