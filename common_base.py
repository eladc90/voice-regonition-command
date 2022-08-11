import psutil
import logging
import os
 
################## LOGGER ################


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(message)s')
file_handler = logging.FileHandler('VOR_logger.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

############# UTILS FUNCTIONS ###################


class utils_functions:
    def __init__(self) -> None:
        pass
    
    
    @staticmethod
    def close_process(process_name):
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                proc.kill()    
                
    @staticmethod                
    def get_spotify_path():
        USER_NAME = os.getlogin()
        SPOTIFY_FULL_PATH = r"C:\Users" 
        SPOTIFY_FULL_PATH += '/' + USER_NAME + r"\AppData\Roaming\Spotify\Spotify.exe"
        return SPOTIFY_FULL_PATH

    
################# DATA VARS #################


SPOTIFY_FULL_PATH = utils_functions.get_spotify_path()