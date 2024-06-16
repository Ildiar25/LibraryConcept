
from utilities.classes.library_class import Library


def menu():
    pass


def main():

    library = Library()

    print("¿Qué desea hacer?")
    menu()


if __name__ == "__main__":
    print(150*"=")
    print("||{:^146}||".format(" ¡BIENVENIDO A LA LIBRERÍA PASTOR! "))
    print(150 * "=")

    main()

    print(150 * "=")
    print("||{:^146}||".format(" ¡GRACIAS! ¡VUELVA PRONTO! "))
    print(150 * "=")
    # libreria = Library()
    #
    # libreria.load_books()
    #
    # libreria.add_book(123456789, "Fantasia 2000", "Alice Wagner", "comedy")
    # libreria.add_book(246813579, "50 Shadows of Gray", "Someone", "drama")
    # libreria.add_book(123459876, "How to care your plants", "Thomas A. Willis", "documental")
    #
    # libreria.save_books()
    # libreria.load_clients()
    #
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
