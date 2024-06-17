
from utilities.log_config import *
import csv

# Create our logger from FileManager to work with
logger = logging.getLogger(__name__)


class FileManager:

    def __init__(self, filepath: str) -> None:
        """
        This builder allows to create an object with the file path given.
        :param filepath: string directory and file name with extension
        """
        self.filepath = filepath
        logger.info(f"New FileManager-type object created!")
        logger.debug(f"CONTENT: {self.__dict__}")

    # Main methods
    def create(self) -> None:
        """
        This function allows to create new file depending on the filepath.
        :return: None
        """
        name = self.filepath.split("/")
        logger.debug(f"{name=}")

        try:
            open(self.filepath, "x").close()
            print("\nArchivo creado con éxito!")
            logger.info(f"New file '{name[-1]}' created!")

        except PermissionError as err:
            logger.error(err)
            print(f"\n[{type(err).__name__}]#### ¡No se tienen permisos para crear el archivo!")
        except FileExistsError as err:
            logger.error(err)
            print(f"\n[{type(err).__name__}]#### ¡El archivo ya existe!")
        except Exception as err:
            logger.error(err)
            print(f"\n[{type(err).__name__}]#### ¡Un error inesperado a ocurrido al intentar crear!")

    def save(self, new_data: list[tuple]) -> None:
        """
        This function allows to save data in a 'csv' file.
        :param new_data: a tuple-type list with different vlues
        :return: None
        """
        try:
            with open(self.filepath, "w", encoding="utf-8", newline="") as file_saved:
                add_data = csv.writer(file_saved, delimiter=";")
                logger.info(f"File '{self.filepath}' open and ready to write!")

                for row in new_data:
                    add_data.writerow(row)

                logger.info(f"File '{self.filepath}' writen successfully!")

        except PermissionError as err:
            logger.error(err)
            print(f"\n[{type(err).__name__}]#### ¡El archivo ya está abierto y no se puede modificar!")
        except Exception as err:
            logger.error(err)
            print(f"\n[{type(err).__name__}]#### ¡Un error inesperado a ocurrido al intentar guardar!")

    def open(self) -> list[list]:
        """
        This function allows to open a 'csv' file and return its data in a list.
        :return: a list with nested lists
        """
        name = self.filepath.split("/")
        row_list = []
        logger.debug(f"{name=}")

        try:
            with open(self.filepath, "r", encoding="utf-8") as file_info:
                row = csv.reader(file_info, delimiter=";")
                logger.info(f"File '{name[-1]}' readed successfully!")

                for info_list in row:
                    row_list.append(info_list)

                logger.info(f"Data from '{name[-1]}' loaded successfully!")

        except FileNotFoundError as err:
            logger.error(err)
            print(f"\n[{type(err).__name__}]#### ¡No se ha encontrado el archivo!")
        except Exception as err:
            logger.error(err)
            print(f"\n[{type(err).__name__}]#### ¡Un error inesperado a ocurrido al intentar cargar!")

        else:
            logger.debug(f"{row_list=}")
            return row_list
