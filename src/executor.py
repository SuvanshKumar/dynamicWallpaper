import datetime
import json
import logging

from src import theme_utils

logger = logging.getLogger(__name__)

def execute(root_path):
	themes = theme_utils.load_theme(root_path)
	
	current_theme_id = themes['currentTheme']
	logger.debug('current_theme_id: ' + current_theme_id)
	
	current_theme = theme_utils.find_theme_by_id(current_theme_id, themes)
	logger.debug('current_theme: ' + str(current_theme))

	current_theme_config = theme_utils.load_config(root_path, current_theme)
	logger.debug('current_theme_config: ' + str(current_theme_config))