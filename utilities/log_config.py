import logging
from utilities.utl import LOGS_FILE

# ----- LEVELS ----- #

# DEBUG: Detailed information, typically only of interest to a developer trying to diagnose a problem.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication about a problem might occur in the near future (e.g. ‘disk space low’).
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# ----- DOCUMENTATION ----- #

# https://docs.python.org/3/library/logging.html

logging.basicConfig(level=logging.WARNING,
                    filename=f"resources/{LOGS_FILE}",
                    filemode="a",
                    encoding="utf-8",
                    datefmt="%d/%m/%y · %H:%M:%S",
                    format="[%(asctime)s] = %(levelname)s at line %(lineno)d from <%(module)s>: %(message)s")

# Here I am trying to give a basic configuration to our logger. Then I will import it from here.
