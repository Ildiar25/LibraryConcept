
from utilities.classes.library_class import Library


def meh():
    pass


def finish():
    pass


def start():
    pass


def client_request():
    pass


def menu():
    pass


def main():

    library = Library()

    print("¿Qué desea hacer?")

    # library.add_book(123456789, "Fantasia 2000", "Alice Wagner", "comedy")
    # library.add_book(246813579, "50 Shadows of Gray", "Someone", "drama")
    # library.add_book(123459876, "How to care your plants", "Thomas A. Willis", "documental")
    #
    # print("¿Desea guardar?")
    #
    # library.save_books()

    library.load_books()


if __name__ == "__main__":
    print(150*"=")
    print("||{:^146}||".format(" ¡BIENVENIDO A LA LIBRERÍA PASTOR! "))
    print(150 * "=")

    start()

    main()

    finish()

    print(150 * "=")
    print("||{:^146}||".format(" ¡GRACIAS! ¡VUELVA PRONTO! "))
    print(150 * "=")

    # libreria.add_client("21123456T", "Thomas", "Wellghinton")
    # libreria.add_client("21356784H", "Sarah", "O'conell")
    # libreria.add_client("21748596F", "Bob", "Miner")
    #
    # libreria.save_clients()
    #
    # book = libreria.look_for_book(123456789)
    # print(book)
    #
    # client = libreria.look_for_client("21123456T")
    # print(client)
    #
    # print("\nLista de libros:")
    # print(f"{[b_added.title for b_added in libreria.book_list]}")
    #
    # print("\nLista de clientes:")
    # print(f"{[c_name.name for c_name in libreria.client_list]}")
