# ----- CONSTANTS -----

BOOKS_FILE = "books.csv"
CLIENTS_FILE = "clients.csv"
LOGS_FILE = "library_logs.log"
SYMBOLS = ('\\', '/', '*', '<', '>', '|', '"', '[', ']', '{', '}', '+', '_', ';', '@', '#', '~', '^', '=', '¬')


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

    not_symbol = True
    answer = input(f"\nIntroduce un texto de entre {min_len} y {max_len} caracteres: ").lower()
    answer = answer.strip()

    for character in answer:
        if character in SYMBOLS:
            not_symbol = False

    if len(answer) == 0:
        print("No se puede dejar el campo vacío.")
        return insert_text(min_len, max_len)

    else:
        if min_len <= len(answer) <= max_len and not_symbol:
            return answer

        else:
            print(f"Lo siento, pero '{answer}' no es un texto válido.")
            print(f"Recuerda, tiene que tener entre {min_len} y {max_len} caracteres además de que no puede contener "
                  f"los siguientes símbolos:")
            print(f"[{" ".join(SYMBOLS)}]")
            return insert_text(min_len, max_len)


def insert_dni() -> str:

    answer = input(f"\nIntroduce un número DNI válido: ").upper()

    if len(answer) == 9 and answer[-1].isalpha():
        return answer
    else:
        print(f"Lo siento, '{answer}' no es un número de DNI válido.")
        return insert_dni()


def insert_option(text_format: str, possible_answers: list[str]):

    answer = input(f"\n{text_format} ({"·".join(possible_answers)}): ").upper()

    if answer in possible_answers:
        return answer

    else:
        print(f"Lo siento, '{answer}' no es un comando válido.")
        return insert_option(text_format, possible_answers)
