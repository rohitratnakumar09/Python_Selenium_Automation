
import os
import logging
import json
from Utilities.config_utility import config_utility
import Utilities.logger_utility as log_utils
class Locators:
    log = log_utils.custom_logger(logging.INFO)


    config = config_utility()
    prop = config.load_config_file()
    base_test_data = prop.get('PROD', 'locators')
    directory = os.path.dirname(os.getcwd())
    locator_dir=os.path.join(directory,base_test_data)
    def __init__(self,filename):
        self.filename=filename
        self.ui_file_path = os.path.join(self.directory, self.locator_dir)

    def read_json(self):
        file=os.path.join(self.locator_dir,self.filename)
        with open(file) as fh:
            jsonfile=json.load(fh)
        return jsonfile
    def page_locators(self,page,locator_name):
        json_data=self.read_json()
        page_locator=[locator for locator in json_data if locator['page_name'] in page]
        for locator in page_locator:
            if locator['name']==locator_name:
                return locator['locate'],locator['locator']
