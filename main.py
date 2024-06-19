
from utilities.classes.library_class import Library
from utilities.utl import *
import time
import os


##### CLIENT SECTION #####
def new_client() -> None:
    pass


def delete_client() -> None:
    pass


def update_client() -> None:
    pass


def show_clients() -> None:

    if len(library.client_list) == 0:
        print("\nActualmente esta biblioteca no dispone de clientes que mostrar.\n")

    else:
        print()
        print(150 * "=")
        print("||{:<146}||".format(" ~~ CLIENTES ACTUALES ~~ "))
        print(150 * "=")

        time.sleep(0.2)
        print("\n\n")

        # Prepare header
        format_ident = "{:^12}".format(" --DNI-- ")
        format_name = "{:^80}".format("--NOMBRE--")
        format_books = "{:^44}".format("--TÍTULOS PRESTADOS--")
        format_quantity = "{:^5}".format("--HUECO--")

        print(150 * "=")
        print(150 * "-")
        print(f"||{format_ident}|{format_name}|{format_books}|{format_quantity}||")
        print(150 * "-")

        library.show_clients()

        print(150 * "-")
        print("\n\n")


##### BOOK SECTION #####
def new_book() -> None:
    # We load all isbns from the book_list
    isbn_list = [book.isbn for book in library.book_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ NUEVO LIBRO ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara agregar un nuevo libro a la biblioteca se deben disponer de los siguientes datos:\n"
          " · ISBN del libro a agregar\n"
          " · El título del mismo\n"
          " · Su autor\n"
          " · Y el género al que pertenece.")

    print("Primero vamos a  comprobar si el ISBN que se va a introducir existe:")

    isbn = insert_number(9)

    if isbn not in isbn_list:
        print("\n¡Perfecto!\n"
              "A partir de ahora, simplemente rellena los campos. No te preocupes si te equivocas.\n"
              "¡Más adelante podrás modificar los datos del libro!\n"
              "\nTÍTULO:")
        title = insert_text(5, 150)
        print("\nAUTOR:")
        author = insert_text(5, 100)
        print("\nGÉNERO:")
        genre = insert_text(5, 20)

        library.add_book(isbn, title, author, genre)

    else:
        print("\n¡No se puede agregar un ISBN que ya existe!\n")


def delete_book() -> None:
    # We load all isbns from the book_list
    isbn_list = [book.isbn for book in library.book_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ ELIMINAR LIBRO ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara eliminar un libro de la biblioteca es necesario aportar un número ISBN.")
    print("\nPor favor, escribe dicho número:")

    required_isbn = insert_number(9)

    if required_isbn in isbn_list:
        finded_book = library.look_for_book(required_isbn)

        answer = insert_option(f"Desea eliminar '{finded_book.title.upper()}'?", ["S", "N"])

        if answer == "S":
            library.book_list.remove(finded_book)
        elif answer == "N":
            print("¡De acuerdo!")

    else:
        print("\n¡Ese ISBN no pertenece a ningún libro almacenado en esta biblioteca!\n")


def update_book() -> None:
    # We load all isbns from the book_list
    isbn_list = [book.isbn for book in library.book_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ MODIFICAR LIBRO ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara modificar un libro de la biblioteca es necesario aportar un número ISBN.")
    print("\nPor favor, escribe dicho número:")

    required_isbn = insert_number(9)

    if required_isbn in isbn_list:
        finded_book = library.look_for_book(required_isbn)

        print(f"\n¡Perfecto! El libro que deseas modificar se titula '{finded_book.title.upper()}'.\n"
              f"¿Qué apartado quieres modificar?\n\n"
              f" · 1) TÍTULO\n"
              f" · 2) AUTOR\n"
              f" · 3) GÉNERO\n"
              f" · 4) CANCELAR")

        answer = insert_option("Selecciona una opción", ["1", "2", "3", "4"])

        if answer == "1":
            print("\n >>> NUEVO TÍTULO:")
            finded_book.title = insert_text(5, 150)
        elif answer == "2":
            print("\n >>> NUEVO AUTOR:")
            finded_book.author = insert_text(5, 100)
        elif answer == "3":
            print("\n >>> NUEVO GÉNERO:")
            finded_book.genre = insert_text(5, 20)
        elif answer == "4":
            print("¡De acuerdo!")

        print(f"¡Datos de '{finded_book.title.upper()}' actualizados!")

    else:
        print("\n¡Ese ISBN no pertenece a ningún libro almacenado en esta biblioteca!\n")


def show_books() -> None:

    if len(library.book_list) == 0:
        print("\nActualmente esta biblioteca no dispone de libros para mostrar.\n")

    else:
        print()
        print(150 * "=")
        print("||{:<146}||".format(" ~~ LIBROS ACTUALES ~~ "))
        print(150 * "=")

        time.sleep(0.2)
        print("\n\n")

        # Prepare header
        format_isbn = "{:-^11}".format(" ISBN ")
        format_title = "{:-^86}".format(" TÍTULO ")
        format_author = "{:-^21}".format(" AUTORÍA ")
        format_genre = "{:-^11}".format(" GÉNERO ")
        format_status = "{:-^13}".format(" ESTADO ")

        print(150 * "=")
        print(f"||{format_isbn}|{format_title}|{format_author}|{format_genre}|{format_status}||")

        library.show_books()

        print(150 * "=")
        print("\n\n")


##### MAIN SECTIONS #####
def books() -> None:
    print()
    print("{:_^150}".format(" Sección LIBROS "))

    print("\n >>>>> Opciones Disponibles:\n"
          " · 1) Nuevo Libro\n"
          " · 2) Eliminar Libro\n"
          " · 3) Editar Libro\n"
          " · 4) Mostrar Libros\n"
          " · 5) ATRÁS")

    answer = insert_option("Qué desea hacer?", ["1", "2", "3", "4", "5"])

    if answer == "1":
        new_book()
    elif answer == "2":
        delete_book()
    elif answer == "3":
        update_book()
    elif answer == "4":
        show_books()
    elif answer == "5":
        print("¡De acuerdo!")


def clients() -> None:
    print()
    print("{:_^150}".format(" Sección CLIENTES "))

    print("\n >>>>> Opciones Disponibles:\n"
          " · 1) Nuevo Cliente\n"
          " · 2) Eliminar Cliente\n"
          " · 3) Editar Cliente\n"
          " · 4) Mostrar Clientes\n"
          " · 5) ATRÁS")

    answer = insert_option("Qué desea hacer?", ["1", "2", "3", "4", "5"])

    if answer == "1":
        new_client()
    elif answer == "2":
        delete_client()
    elif answer == "3":
        update_client()
    elif answer == "4":
        show_clients()
    elif answer == "5":
        print("¡De acuerdo!")


def requests() -> None:
    print()
    print("{:_^150}".format(" Sección SOLICITUDES "))

    print("\n >>>>> Opciones Disponibles:\n"
          " · 1) Devolución\n"
          " · 2) Préstamo\n"
          " · 3) Reserva\n"
          " · 4) ATRÁS")

    answer = insert_option("Qué desea hacer?", ["1", "2", "3", "4"])

    if answer == "1":
        pass
    elif answer == "2":
        pass
    elif answer == "3":
        pass
    elif answer == "4":
        print("¡De acuerdo!")


def start_app() -> Library:

    library_init = Library()

    if os.path.isfile(f"resources/{BOOKS_FILE}") and os.path.isfile(f"resources/{CLIENTS_FILE}"):

        print("Cargando libros...")
        time.sleep(0.2)
        library_init.load_books()
        print("\nCargando clientes...")
        time.sleep(0.2)
        library_init.load_clients()
    else:
        print("¡Buenos días!")
        print("¡Parece que es su primera vez en esta app, espero que la experiencia sea de su agrado!")

    return library_init


def main_menu() -> None:

    working = True

    while working:

        print()
        print("{:^150}".format(20*"_" + " Secciones Disponibles " + 20*"_"))
        print(150 * "=")
        print("||{:^35}".format("LIBROS") +
              "||{:^35}".format("CLIENTES") +
              "||{:^35}".format("SOLICITUD") +
              "||{:^35}".format("SALIR") + "||")
        print(150 * "=")
        print("\n¿Qué sección deseas visitar?")
        answer = input().upper()

        if answer == "LIBROS":
            books()
        elif answer == "CLIENTES":
            clients()
        elif answer == "SOLICITUD":
            requests()
        elif answer == "SALIR":
            working = False
        else:
            print(f"Lo siento, '{answer}' no es un comando válido.")


def close_app() -> None:

    print("Guardando datos antes de cerrar...")
    library.save_books()
    time.sleep(1)
    library.save_clients()
    time.sleep(1)


if __name__ == "__main__":
    print(150 * "=")
    print("||{:^146}||".format(" ¡BIENVENIDO A LA LIBRERÍA PASTOR! "))
    print(150 * "=")

    library = start_app()

    main_menu()

    close_app()

    print(150 * "=")
    print("||{:^146}||".format(" ¡GRACIAS! ¡HASTA LUEGO! "))
    print(150 * "=")
