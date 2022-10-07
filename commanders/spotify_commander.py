from asyncio import subprocess
from .app_command import App_command
from spotify_files.spotify_api import Spotify_API
from common_base import SPOTIFY_FULL_PATH
import psutil
import subprocess
import os

class Spotify_commander(App_command):
    def __init__(self, app_status=True, app_key='spotify'):
        super().__init__(app_status, app_key)
        self._Spotify_API = Spotify_API()
        self.command_dict = {
            'next song':        self._next_song,
            'next':             self._next_song,
            'previous song':    self._previous_song,
            'pause song':       self._pause_song,
            'play song':        self._play_song,
            'play':             self._play_song,
            'stop song':        self._pause_song,
            'stop':             self._pause_song,
            'close spotify':    self._close_spotify_app,
            'open spotify':     self._open_spotify_app,
            'spotify look for': self._look_for_song,
            'look for':         self._look_for_song, 
            'luke for':         self._look_for_song, 
        }
        self._prefix_command_list = ['spotify look for', 'look for', 'luke for']
        
        
    # def Get_command(self, command):   
    #     for key, val in self.command_dict.items():
    #         if key == command and key not in self._prefix_command_list:
    #             val(command)
                
          
    def _next_song(self, command):
        self._Spotify_API.next_song()
        
        
    def _previous_song(self, command):
        self._Spotify_API.previous_song()
        
    
    def _pause_song(self, command):
        self._Spotify_API.pause_song()
        
        
    def _play_song(self, command):
        self._Spotify_API.play_song()
        
      
    def _look_for_song(self, command):
        command_prefix = None
        for key, val in self.command_dict.items():
            if val == self._look_for_song:
                if command.startswith(key):
                    command_prefix = key
                    break
                    
        if command_prefix is None or command_prefix == ' ':
            print('cant get song name')
        
        song_name = command.replace(key, '').strip()
        print(f"looking for {song_name}")
        self._Spotify_API.search_song(song_name)
      
      
    def _open_spotify_app(self, command):
        is_open = self._is_spotify_open()
        if is_open is True:
            print('spotify already open')
        else:
            subprocess.Popen([SPOTIFY_FULL_PATH], shell=True)

                
    def _close_spotify_app(self, command):
        os.system('taskkill /f /im "Spotify.exe" ')   
    
                
#==============================================#
#               AID FUNCTIONS                  #
#==============================================#


    def _is_spotify_open(self):
        for process in psutil.process_iter():
            if process.name() == 'Spotify.exe':
                return True
        return False    


if __name__ == '__main__':
    spo = Spotify_commander()
    spo._close_spotify_app(2)