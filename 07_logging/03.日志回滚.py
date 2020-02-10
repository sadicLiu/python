import logging
from logging.handlers import RotatingFileHandler

# notes: 记录日志产生异常时,可能会出现记录了很多无用日志的情况,这时候记下的日志就没有意义了
#   RotatingFileHandler可以完成日志文件的切割

logger = logging.getLogger("log")
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 定义一个RotatingFileHandler,最多备份3个日志文件,每个日志文件最大1K
rHandler = RotatingFileHandler("log3.txt", maxBytes=1 * 1024, backupCount=3)
rHandler.setLevel(logging.INFO)
rHandler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(rHandler)
logger.addHandler(console)

for i in range(10000):
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
