import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    logging.debug("testing debug logging")
    logging.info("testing info logging")
    logging.warning("testing warning logging")
    logging.critical("testing critical logging")
    logging.fatal("testing fatal logging")