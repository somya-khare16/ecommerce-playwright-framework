import logging
from pathlib import Path

LOGS_FOLDER = Path("logs")
LOG_FILE = LOGS_FOLDER / "test_execution.log"


def get_logger(name: str) -> logging.Logger:
    LOGS_FOLDER.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(LOG_FILE,encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
#   Prevents the same message from being passed to other loggers higher up in Python’s logging system.
#   This is another protection against duplicate log messages.
    logger.propagate = False

    return logger
  