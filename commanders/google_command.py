from asyncio.log import logger
from .app_command import App_command
import subprocess
import pyperclip


class Google_commander(App_command):
    """commander to use google search
    
    the voice command has to start with google. the command arrive to the google dispatch function
    witch execute the correct function by the command received
    
    
    voice command:
        - 'google' + any words -> use to open google and search the words
        - 'google it' -> use to search whatever in clipboard (ctrl + c)

    """
    
    def __init__(self, app_status=True, app_key='google'):
        super().__init__(app_status, app_key)
        self.command_dict = {
            'google': self._google_command_dispatch,
            }


    def _google_command_dispatch(self, command):
        if command == 'google it':
            self._google_from_copy(command)
        else:
            self._open_chrome_google_search(command)
            
     
    def _open_chrome_google_search(self, command):
        try:
            google_search_cmd = 'start chrome https://www.google.com/search?q='
            search_word_list = command.split()
            try:
                search_word_list.remove('google')
            except ValueError:
                pass
            for word in search_word_list:
                google_search_cmd += word + '+'
            subprocess.Popen(google_search_cmd, shell=True)
        except Exception as ex:
            logger.info(ex)
            
        
    def _google_from_copy(self, command):
        data_to_search = pyperclip.paste()
        self._open_chrome_google_search(data_to_search)
        
        
