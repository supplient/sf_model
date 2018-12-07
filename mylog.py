import logging
import sys

log = logging.getLogger("sf_model")
log.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(levelname)s] %(message)s")

file_handler = logging.FileHandler("log/debug.log", "wt")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
log.addHandler(file_handler)

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(logging.WARNING)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)