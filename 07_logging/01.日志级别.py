import logging

# 日志级别: debug,info,warning,error,critical,fatal

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("logger")

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.error("Error occured")
logger.critical("Program collapse")
logger.info("Finish")
