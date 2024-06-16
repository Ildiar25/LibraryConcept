# ----- CONSTANTS -----

BOOKS_FILE = "books.csv"
CLIENTS_FILE = "clients.csv"
SYMBOLS = ('\\', '/', '*', '<', '>', '|', '"', '[', ']', '{', '}', '+', '_', ';')


# ----- FUNCTIONS -----

def insert_number(max_len: int) -> int:

    answer = input(f"\nIntroduce un número de {max_len} cifras: ")

    if answer.isdigit():
        if len(answer) == max_len:
            return int(answer)
        else:
            print("Ese número no sirve.")
            return insert_number(max_len)
    else:
        print(f"'{answer}' no es un número válido.")
        return insert_number(max_len)


def insert_text(min_len: int, max_len: int) -> str:

    answer = input(f"\nIntroduce un texto de entre {min_len} y {max_len} caracteres: ").lower()

    if min_len <= len(answer) <= max_len:
        if answer.isspace():
            print("No se puede dejar en blanco.")
            return insert_text(min_len, max_len)

        else:
            has_symbol = False

            for element in answer:
                if element in SYMBOLS:
                    has_symbol = True

            if has_symbol:
                print("El texto no puedo contener niguno de los siguientes símbolos:")
                print(SYMBOLS)
                return insert_text(min_len, max_len)

            else:
                return answer

    else:
        print(f"{answer} no es un texto válido.")
        return insert_text(min_len, max_len)


def insert_dni() -> str:

    answer = input(f"\nIntroduce un número DNI válido: ").upper()

    if len(answer) == 9 and answer[-1].isalpha():
        return answer
    else:
        print(f"Lo siento, '{answer}' no es un número de DNI válido.")
        return insert_dni()

