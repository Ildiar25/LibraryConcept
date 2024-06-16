
from utilities.log_config import *

import datetime

# Create our logger from Event to work with
logger = logging.getLogger(__name__)


class Event:

    def __init__(self, customer: str, event: str) -> None:

        self.customer = customer
        self.event = event
        self.date: datetime = datetime.datetime.now()
        logger.debug("New Event-type object created.")
