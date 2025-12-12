# import logging
# import os
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
import logging
import os

class LogGen:
    @staticmethod
    def loggen():

        # Ensure Logs directory exists
        if not os.path.exists("Logs"):
            os.makedirs("Logs")

        log_path = os.path.join("Logs", "automation.log")

        logger = logging.getLogger("nopCommerce")
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers (duplicate logs)
        if not logger.handlers:
            fh = logging.FileHandler(log_path, mode="a")
            formatter = logging.Formatter(
                "%(asctime)s: %(levelname)s: %(message)s",
                "%m/%d/%Y %I:%M:%S %p"
            )
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger
