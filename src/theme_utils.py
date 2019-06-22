import os
import json
import logging

logger = logging.getLogger(__name__)

def load_theme(root_path):
    '''Reads the themes.json file and returns the dict object.'''
    with open(root_path+('/themes.json')) as theme_file:
        themes = json.load(theme_file)
        logger.debug(str(themes))
        return themes

def find_theme_by_id(id, themes):
    '''
    Finds the theme by id, and returns a dict containing id, name, config, pictures.

    Returns None if the theme is not found
    Raises TypeError if the themes object is not of the same type as themes.json converted to native python datatype (using json.load)
    Raises ValueError if any of the expected keys are missing
    '''
    # TODO: check for the datatype of the currentTheme -- it should be a string
    # TODO: check for the datatype of the allTheme -- it should be a list of dicts
    # each of those dicts should have 'id', 'name', 'confic', 'pictures' keys atleast (or exactly?)
    for theme in themes['allThemes']:
        
        if theme['id'] == id:
            logger.debug('Theme: ' + str(theme))
            return theme
        
        logger.debug('No theme found')

    return None

def load_config(root_path, current_theme):
    '''
    Loads the config json file of the theme

    Parameter:
    Either pass the current_theme dict (which is the loaded dict from themes.json, then extracted the value of allThemes key, and then a dict from that list
    Or pass the string containing the path of the config.json file from the root_path'''
    # TODO: check if current_theme is dict, then it should have 'id', 'name', 'config', 'pictures' keys and all their values should be of type strings.
    file_path = None
    if isinstance(current_theme, dict):
        file_path = current_theme['config']
    elif isinstance(current_theme, str):
        file_path = current_theme
    if file_path is not None:
        logger.debug('Config file path: ' + file_path)
        with open(os.path.join(root_path, file_path)) as config_file:
            config = json.load(config_file)
    else:
        logger.debug('Config file path not found')
        raise TypeError('Current_theme may either be a theme type dict, or a string denoting the path of the config json file')
    return config