import inspect
import logging

class LogGen:
    @staticmethod
    def loggen(logLevel=logging.DEBUG):
        #Set Class/method name from where it's called
        logger_name=inspect.stack()[1][3]
        #create logger
        logger=logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        #create console handler or file handler and set the log level
        fh=logging.FileHandler("../Logs/automation.log")
        #create formatter -how you want your logs to be formatted
        formatter=logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or file handler
        fh.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(fh)
        return logger

"""
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='../Logs/automation.log', format='%(asctime)s:%(level)s:%(message)s',
                            datefmt='%m/%d%/%Y %I:%M:%S %p', filemode='w')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
"""