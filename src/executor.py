import datetime
import json
import logging

from src import theme_loader

logging.basicConfig(level = logging.DEBUG, filename = '/media/suvansh/E/Projects/dynamicWallpaper/exec.log')

def execute(root_path):
    with open(root_path+('/themes.json')) as theme_file:
        themes = json.load(theme_file)
        logging.debug(themes)
