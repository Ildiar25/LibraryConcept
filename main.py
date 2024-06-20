
from utilities.classes.library_class import Library
from utilities.utl import *
import time
import os


##### REQUEST SECTION #####
def book_return() -> None:
    # We load all necessary data
    ident_list = [client.ident for client in library.client_list]
    isbn_list = [book.isbn for book in library.book_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ DEVOLUCIÓN ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara realizar una devolución se deben disponer de los siguientes datos:\n"
          " · DNI del cliente que solicita la petición\n"
          " · El ISBN del libro a devolver.")

    print("Primero vamos a seleccionar al cliente mediante su DNI:")

    ident = insert_dni()

    if ident in ident_list:

        client_request = library.look_for_client(ident)
        print(f"\n¡Gracias {client_request.name.capitalize()}! ¿Qué libro quieres devolver?")
        print("Por favor, introduce su ISBN en el siguiente campo:")

        isbn_request = insert_number(9)

        if isbn_request in isbn_list:
            returned_book = library.look_for_book(isbn_request)
            print(f"\n¡Se va a devolver el libro titulado '{returned_book.title.upper()}'!")
            client_request.give_back(returned_book)

        else:
            print("\n¡Ese ISBN no pertenece a ningún libro almacenado en esta biblioteca!\n")

    else:
        print("\n¡Ese DNI no pertenece a ningún cliente registrado en esta biblioteca!\n")


def book_lending() -> None:
    # We load all necessary data
    ident_list = [client.ident for client in library.client_list]
    isbn_list = [book.isbn for book in library.book_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ PRÉSTAMO ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara realizar una prestación se deben disponer de los siguientes datos:\n"
          " · DNI del cliente que solicita la petición\n"
          " · El ISBN del libro a prestar.")

    print("Primero vamos a seleccionar al cliente mediante su DNI:")

    ident = insert_dni()

    if ident in ident_list:

        client_request = library.look_for_client(ident)
        print(f"\n¡Gracias {client_request.name.capitalize()}! ¿Qué libro quieres pedir prestado?")
        print("Por favor, introduce su ISBN en el siguiente campo:")

        isbn_request = insert_number(9)

        if isbn_request in isbn_list:
            lended_book = library.look_for_book(isbn_request)
            print(f"\n¡Se van a llevar el libro titulado '{lended_book.title.upper()}'!\n")

            answer = insert_option("¿Quieres llevarte este libro?", ["S", "N"])

            if answer == "S":
                client_request.take_away(lended_book)
            elif answer == "N":
                print("¡De acuerdo!")

        else:
            print("\n¡Ese ISBN no pertenece a ningún libro almacenado en esta biblioteca!\n")

    else:
        print("\n¡Ese DNI no pertenece a ningún cliente registrado en esta biblioteca!\n")


def book_reserve() -> None:
    # We load all necessary data
    ident_list = [client.ident for client in library.client_list]
    isbn_list = [book.isbn for book in library.book_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ RESERVA ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara realizar una reserva se deben disponer de los siguientes datos:\n"
          " · DNI del cliente que solicita la petición\n"
          " · El ISBN del libro a prestar.")

    print("Primero vamos a seleccionar al cliente mediante su DNI:")

    ident = insert_dni()

    if ident in ident_list:

        client_request = library.look_for_client(ident)
        print(f"\n¡Gracias {client_request.name.capitalize()}! ¿Qué libro quieres reservar?")
        print("Por favor, introduce su ISBN en el siguiente campo:")

        isbn_request = insert_number(9)

        if isbn_request in isbn_list:
            reserved_book = library.look_for_book(isbn_request)
            print(f"\n¡Se va a reservar el libro titulado '{reserved_book.title.upper()}'!\n")

            answer = insert_option("¿Quieres reservar este libro?", ["S", "N"])

            if answer == "S":
                client_request.save_book(reserved_book)
            elif answer == "N":
                print("¡De acuerdo!")

        else:
            print("\n¡Ese ISBN no pertenece a ningún libro almacenado en esta biblioteca!\n")

    else:
        print("\n¡Ese DNI no pertenece a ningún cliente registrado en esta biblioteca!\n")


##### CLIENT SECTION #####
def new_client() -> None:
    # We load all NIEs from the client_list
    ident_list = [client.ident for client in library.client_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ NUEVO CLIENTE ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara agregar un nuevo cliente al registro se deben disponer de los siguientes datos:\n"
          " · DNI del cliente a agregar\n"
          " · El nombre del mismo\n"
          " · Y su apellido.")

    print("Primero vamos a comprobar si el DNI que se va a introducir existe:")

    ident = insert_dni()

    if ident not in ident_list:
        print("\n¡Perfecto!\n"
              "A partir de ahora, simplemente rellena los campos. No te preocupes si te equivocas.\n"
              "¡Más adelante podrás modificar los datos del cliente!\n"
              "\nNOMBRE COMPLETO:")
        name = insert_text(3, 20)
        print("\nAPELLIDOS:")
        surname = insert_text(3, 50)

        library.add_client(ident, name, surname)

    else:
        print("\n¡No se puede agregar un DNI que ya existe!\n")


def delete_client() -> None:
    # We load all NIEs from the client_list
    ident_list = [client.ident for client in library.client_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ ELIMINAR CLIENTE ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara eliminar un cliente del registro es necesario aportar un número de DNI.")
    print("\nPor favor, escribe dicho número:")

    required_ident = insert_dni()

    if required_ident in ident_list:
        finded_client = library.look_for_client(required_ident)

        answer = insert_option(f"Desea eliminar '{finded_client.name.upper()}'?", ["S", "N"])

        if answer == "S":
            library.client_list.remove(finded_client)
        elif answer == "N":
            print("¡De acuerdo!")

    else:
        print("\n¡Ese DNI no pertenece a ningún cliente registrado en esta biblioteca!\n")


def update_client() -> None:
    # We load all NIEs from the client_list
    ident_list = [client.ident for client in library.client_list]

    print()
    print(150 * "=")
    print("||{:<146}||".format(" ~~ MODIFICAR CLIENTE ~~ "))
    print(150 * "=")

    time.sleep(1)
    print("\nPara modificar un cliente del registro es necesario aportar un número de DNI.")
    print("\nPor favor, escribe dicho número:")

    required_ident = insert_dni()

    if required_ident in ident_list:
        finded_client = library.look_for_client(required_ident)

        print(f"\n¡Perfecto! El cliente que deseas modificar se llama '{finded_client.name.upper()}'.\n"
              f"¿Qué apartado quieres modificar?\n\n"
              f" · 1) NOMBRE\n"
              f" · 2) APELLIDOS\n"
              f" · 3) CANCELAR")

        answer = insert_option("Selecciona una opción", ["1", "2", "3"])

        if answer == "1":
            print("\n >>> NUEVO NOMBRE:")
            finded_client.name = insert_text(3, 20)
        elif answer == "2":
            print("\n >>> NUEVOS APELLIDOS:")
            finded_client.surname = insert_text(3, 50)
        elif answer == "3":
            print("¡De acuerdo!")

        print(f"¡Datos de '{finded_client.name.upper()}' actualizados!")

    else:
        print("\n¡Ese DNI no pertenece a ningún cliente registrado en esta biblioteca!\n")


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
        format_ident = "{:-^13}".format(" DNI ")
        format_name = "{:-^81}".format(" NOMBRE ")
        format_books = "{:-^44}".format(" TÍTULOS PRESTADOS ")
        format_quantity = "{:-^5}".format("HUECO")

        print(150 * "=")
        print(f"||{format_ident}|{format_name}|{format_books}|{format_quantity}||")

        library.show_clients()

        print(150 * "=")
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

    print("Primero vamos a comprobar si el ISBN que se va a introducir existe:")

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


##### MAIN SECTION #####
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
        book_return()
    elif answer == "2":
        book_lending()
    elif answer == "3":
        book_reserve()
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
