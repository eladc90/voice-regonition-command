from .app_command import App_command
from common_base import *
import subprocess


class translate_commander(App_command):
    def __init__(self, app_status=True, app_key='translate'):
        super().__init__(app_status, app_key)
        self.command_dict = {
            'morfix':           self._translate_with_morfix,
            'translate': self._google_translate
        }

    def _google_translate(self, command):
        try:
            google_search = r'start chrome https://translate.google.co.il/?hl=iw"&"sl=auto"&"tl=iw"&"text='
            search_word_list = command.split()
            try:
                search_word_list.remove('translate')
            except ValueError:
                pass
            for word in search_word_list:
                google_search += word + r'%20'
            google_search += r'"&"op=translate'
            print(google_search)
            subprocess.Popen(google_search, shell=True)
        except Exception as ex:
            print("in exception")
            logger.info(ex)
            
            
    def _translate_with_morfix(self, command):
        try:
            morfix_search = 'start chrome https://www.morfix.co.il/'
            search_word_list = command.split()
            try:
                search_word_list.remove('morfix')
            except ValueError:
                pass
            for word in search_word_list:
                morfix_search += word + '%20'
            subprocess.Popen(morfix_search, shell=True)
        except Exception as ex:
            logger.info(ex)