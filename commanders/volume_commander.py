from .app_command import App_command
from volume_files.volume_change import Volume_change



class volume_commander(App_command):
    def __init__(self, app_status=True, app_key='volume'):
        super().__init__(app_status, app_key)
        self.volume = Volume_change()
        self.command_dict = {
            
            'volume': self._dispatch_commands,
            'mute': self._mute
        }
                
    def _volume_up(self, command):
        self.volume.volume_up()
        
    def _dispatch_commands(self, command: str) -> None:
        print("in dispath command")
        if command == 'volume up':
            self._volume_up(command)
        elif command == 'volume down':
            self._volume_down(command)
        else:
            
            
            
            
            split_command = command.split('volume ')
            print(split_command)
            print(split_command[1].isdigit())
            if len(split_command) > 1 and split_command[1].isdigit():
                self._set_value(int(split_command[1]))
            
    def _mute(self, command) -> None:
        self.volume.mute()
        
    def _volume_down(self, command):    
        self.volume.volume_down()
        
        
        
    
    def _set_value(self, value: int) -> None:
        print(f'setttings to {value}')
        self.volume.set_volume_value(value)