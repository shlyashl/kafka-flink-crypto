import logging


formatter = logging.Formatter(
    "%(asctime)-18s | %(levelname)-8s | %(module)-15s | %(funcName)-15s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
log = logging.getLogger("logger")
log.setLevel(logging.DEBUG)
log.addHandler(handler)
