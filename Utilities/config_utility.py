import os
import logging
from configparser import ConfigParser
import Utilities.logger_utility as log_utils

class config_utility:
    """
    This class includes basic reusable config_helpers.
    """
    log = log_utils.custom_logger(logging.INFO)
    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.config_path = os.path.join(self.cur_path, r"../Config/config.ini")
    def load_config_file(self):
        """
        This method loads the config/ini file
        :return: this method returns config reader instance.
        """
        config = None
        try:
            config = ConfigParser()
            config.read(self.config_path)
        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
        return config
