from abc import abstractmethod
from app_container import App_container


class App_command:
    def __init__(self, app_status=True, app_key=None, app_container=None):
        """the app command use to send command to app if get command from the voice recognition.
        this class is a base class use to implement by avery new app.
        
        the status variable made to indicate if the app command is on or off (True or False respectively).
        if the app is on class collect text command and try to execute command if possible.   

        Args:
            app_status (bool, optional): App is off or on. Defaults to True.
            
            
            self.command_dict should contains the function to execute with their relative key (command) 
            that execute the function for example:
                the key (command) of the next song function is 'next song' so when this command received 
                the self.command_dict should contain the functions. every executer function need to be from the following shape -> def name_of_function(self, command):
                
                example of full self.command_dict: 
                
                        ===============================================================================
                        
                                self.command_dict = {
                                      'next song': self._next_song,
                                      'previous song': self._previous_song,
                                      'pause song': self._pause_song,
                                      'play song': self._play_song
                                  }


                              def _next_song(self, command):
                                  self._Spotify_API.next_song()


                              def _previous_song(self, command):
                                  self._Spotify_API.previous_song()


                              def _pause_song(self, command):
                                  self._Spotify_API.pause_song()


                              def _play_song(self, command):
                                  self._Spotify_API.play_song()
                                  
                                  
                        ===============================================================================

        """
        
        self._status = app_status
        self.app_key = app_key
        self.app_container = app_container
        self.command_dict = {}
        
    def set_status(self, app_status):
        self._status = app_status
        
    
    def register_self(self, app_container: App_container):
        self.app_container = app_container
        app_container.register_app(self, self.app_key, self._status)
        print(self._status)
        if self._status == True:
            self.register_as_listener()
    
    
    def register_as_listener(self):
        if self.app_container is None:
            # TODO exception? 
            print("no container to register to!")
        else:
            self.app_container.set_app_as_listener(self.app_key)
            
    
    def on_command(self):
        return self.app_key
    
    
    def Get_command(self, command):
        self.execute_command(command)
        
        
    def execute_command(self, command):
        is_command_work = False
        for key, val in self.command_dict.items():
            if key == command:
                val(command)
                is_command_work = True
        if is_command_work is False:
            for key, val in self.command_dict.items():
                if key in command:
                    val(command)
                    
                    
                    
                    
                    
    
    
