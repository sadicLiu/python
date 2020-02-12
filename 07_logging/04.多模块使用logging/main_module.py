import logging
import sub_module

logger = logging.getLogger("mainModule")
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# formatter = logging.Formatter('%(message)s')

file_handler = logging.FileHandler("log4.txt")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("creating an instance of subModule.subModuleClass")
a = sub_module.SubModuleClass()

logger.info("calling subModule.subModuleClass.doSomething")
a.do_something()

logger.info("done with  subModule.subModuleClass.doSomething")
logger.info("calling subModule.some_function")

sub_module.some_function()
logger.info("done with subModule.some_function")
