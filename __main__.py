import os
import json
import logging

from src import executor

logging_format = '%(levelname)s %(filename)s %(funcName)s - %(message)s'
logging.basicConfig(level = logging.DEBUG, filename = '/media/suvansh/E/Projects/dynamicWallpaper/exec.log', format = logging_format)

_root_path = os.path.dirname(os.path.realpath(__file__))

executor.execute(_root_path)