from .app_command import App_command
import subprocess

class CMD_commander(App_command):
    def __init__(self, app_status=False, app_key='command'):
        super().__init__(app_status, app_key)
        self.command_dict = {
            'open new window': self._open_chrome,
            'open new windows': self._open_chrome
        }

                
    def _open_chrome(self, command):
        command = 'start chrome'
        subprocess.Popen(command, shell=True)