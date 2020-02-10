import logging
import sys

logger = logging.getLogger("log")
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

# ================ 将日志输出到文件 ==================
file_handler = logging.FileHandler("log2.txt")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# ================ 将日志输出到屏幕 ==================
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# ================ 输出 ==================
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
