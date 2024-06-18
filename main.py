
from utilities.classes.library_class import Library
from utilities.utl import *
import time
import os
import colorama


def new_book() -> None:

    print("\nVamos a agregar un nuevo libro")
    isbn = insert_number(9)
    title = insert_text(5, 150)
    author = insert_text(5, 100)
    genre = insert_text(5, 20)

    library.add_book(isbn, title, author, genre)


def delete_book() -> None:

    print("\nPor favor, introduzca el ISBN del libro que desea eliminar:")
    required_isbn = insert_number(9)
    finded_book = library.look_for_book(required_isbn)

    answer = insert_option(f"Desea eliminar '{finded_book.title.upper()}'?", ["S", "N"])

    if answer == "S":
        library.book_list.remove(finded_book)
    elif answer == "N":
        print("¡De acuerdo!")


def update_book() -> None:

    print("\nPor favor, introduzca el ISBN del libro que desea modificar:")
    required_isbn = insert_number(9)
    finded_book = library.look_for_book(required_isbn)


def show_books() -> None:

    if len(library.book_list) == 0:
        print("No hay libros para mostrar")

    else:
        for book in library.book_list:
            print(book.title)


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
        pass
    elif answer == "2":
        pass
    elif answer == "3":
        pass
    elif answer == "4":
        pass
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
    print("Cargando...")
    time.sleep(1)

    if os.path.isfile(f"resources/{BOOKS_FILE}") and os.path.isfile(f"resources/{CLIENTS_FILE}"):
        library_init.load_books()
        time.sleep(1)
        library_init.load_clients()
    else:
        print("¡Buenos días!")
        print("¡Parece que es su primera vez en esta app, espero que la experiencia sea de su agrado!")

    return library_init


def main_menu() -> None:

    working = True

    while working:

        print()
        print("{:^150}".format(20*"_" + " Seccione una Opción " + 20*"_"))
        print(150 * "=")
        print("||{:^35}".format("LIBROS") +
              "||{:^35}".format("CLIENTES") +
              "||{:^35}".format("SOLICITUD") +
              "||{:^35}".format("SALIR") + "||")
        print(150 * "=")
        print("\n¿Qué quieres hacer?")
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
