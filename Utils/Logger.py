import logging
class log_generator_class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger()
        if not logger.hasHandlers():  # ✅ Avoid adding multiple handlers
            log_file = logging.FileHandler(r"D:\Credence 37 Batch\4. Automation Testing\Docs & Notes\Pytest_Class_Notes\Logs\CredKart_Automation.log", mode='a')
            log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d -  %(message)s')
            log_file.setFormatter(log_format)
            logger.addHandler(log_file)
            logger.setLevel(logging.INFO)
        return logger