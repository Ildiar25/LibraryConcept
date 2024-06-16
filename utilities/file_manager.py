
from utilities.log_config import *
import csv

# Create our logger from FileManager to work with
logger = logging.getLogger(__name__)


class FileManager:

    def __init__(self, filepath: str) -> None:
        """
        This builder allows to create an object with de file path given.
        :param filepath: string directory and file name with extension
        """
        self.filepath = filepath
        logger.debug(f"New filepath-type object created: '{filepath}'")

    # Main methods
    def create(self) -> None:

        name = self.filepath.split("/")
        logger.debug(f"Separation: {name}")

        try:
            open(self.filepath, "x").close()
            logger.info(f"File {name[-1]} created!")
            print("\nArchivo creado con éxito!")

        except PermissionError as err:
            logger.error(err)
            print("\nNo se tienen permisos para crear el archivo!")
        except FileExistsError as err:
            logger.error(err)
            print("\nEl archivo ya existe!")
        except Exception as err:
            logger.error(err)
            print("\nUn error inesperado a ocurrido.")

    def save(self, new_data: list[tuple]) -> None:

        try:
            with open(self.filepath, "w", encoding="utf-8", newline="") as file_saved:
                add_data = csv.writer(file_saved, delimiter=";")

                for row in new_data:
                    add_data.writerow(row)

                logger.debug(f"Books added: {[element[1] for element in new_data]}")

        except PermissionError as err:
            logger.error(err)
            print("\nNo se tienen permisos para modificar el archivo!")
        except Exception as err:
            logger.error(err)
            print("\nUn error inesperado a ocurrido.")

    def open(self) -> list[list]:

        name = self.filepath.split("/")
        row_list = []

        try:
            with open(self.filepath, "r", encoding="utf-8") as file_info:
                row = csv.reader(file_info)
                logger.debug(f"Data readed from '{name[-1]}'")
                logger.debug(f"Data-type: {type(row).__name__.upper()}: DATA : {row}")

                for info_list in row:
                    row_list.append(info_list)
                logger.info(f"Data from {name[-1]} loaded correctly!")

        except FileNotFoundError as err:
            logger.error(err)
            print("\nEl archivo no se encuentra.")
        except Exception as err:
            logger.error(err)
            print("\nUn error inesperado a ocurrido.")

        else:
            return row_list
