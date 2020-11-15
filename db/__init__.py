from logging import getLogger
from typing import List
import sys

log = getLogger('DB')


class Model:
    """
    Base class for all database Models.

    Used to ensure we have included some required features
         and for use in `click` commands.
    """

    __all_models = []

    def __repr__(self) -> str:
        return "<Model {}>".format(self.__name__)

    def __init_subclass__(cls, *args, **kwargs):
        """Run checks on subclassed Models"""
        log.debug(f"Attempting to load Model: {cls.__name__}")

        required_attributes = [
            "create_table",
            "drop_table"
        ]

        if cls.__name__ in cls.__all__model_names():
            sys.stderr.write(f"Model {cls.__name__} has already been registered.")
            exit(1)

        for attr in required_attributes:
            if not hasattr(cls, attr):
                sys.stderr.write(
                    f"Model {cls.__name__} does not have the `{attr}` attribute, exiting..."
                )
                exit(1)

        log.info(f"Loaded model: {cls}")
        cls.__all_models.append(cls)

    @classmethod
    def __all__model_names(cls) -> List[str]:
        return [obj.__name__ for obj in cls.__all_models]
