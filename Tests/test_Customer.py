import shutil
import os
from datetime import datetime
from Utilities.config_utility import config_utility

config = config_utility()
prop = config.load_config_file()

directory = os.path.dirname(os.getcwd())

