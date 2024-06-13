
from utilities.log_config import *

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

    def save(self, new_data: str) -> None:

        try:
            pass

        except Exception as err:
            pass

    def open(self) -> any:

        name = self.filepath.split("/")

        try:
            with open(self.filepath, "r") as file_info:
                data = file_info.read()
                logger.debug(f"Data readed from '{name[-1]}'")

        except FileNotFoundError as err:
            logger.error(err)
            print("\nEl archivo no se encuentra")
        except Exception as err:
            logger.error(err)
            print("\nUn error inesperado a ocurrido.")

        else:
            return data
