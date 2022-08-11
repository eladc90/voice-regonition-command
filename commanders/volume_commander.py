from .app_command import App_command
from volume_files.volume_change import Volume_change



class volume_commander(App_command):
    def __init__(self, app_status=True, app_key='volume'):
        super().__init__(app_status, app_key)
        self.volume = Volume_change()
        self.command_dict = {
            'volume up': self._volume_up,
            'volume down': self._volume_down
        }
                
    def _volume_up(self, command):
        self.volume.volume_up()
        
    
    def _volume_down(self, command):
        self.volume.volume_down()
        