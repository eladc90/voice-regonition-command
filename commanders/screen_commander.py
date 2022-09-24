from .app_command import App_command
from common_base import *
import subprocess
import pyautogui
import os
import time
from PIL import Image
import threading
import queue


class screen_commander(App_command):
    def __init__(self, app_status=True, app_key='screen'):
        super().__init__(app_status, app_key)
        self.command_dict = {
            'black screen': self._black_screen,
            'close screen': self._black_screen,
            'show screen': self._close_screen,
            'screen'     : self._change_state   
            
        }
        self.screen_state = True
           
    def _change_state(self, command):
        if self.screen_state is True:
            self.screen_state = False
            self._black_screen(command)
        else:
            self.screen_state = True
            self._close_screen(command)
            
            
    def _black_screen(self, command):
        self._open_the_black_screen()
        self.screen_state = False
    
        
    def _open_the_black_screen(self):
        im = Image.open(r"./black_screen.jpg") 
        im.show() 
        time.sleep(1)
        pyautogui.press('f11') # full screen


    def _close_screen(self, command):
        if command == 'screen':
            utils_functions.close_process("Microsoft.Photos.exe")
            self.screen_state = False
        


