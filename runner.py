from distutils.cmd import Command
import time
import speech_recognition
from recognizer_google import Mic_listener
from app_container import App_container
from commanders.text_commander import text_commander
from commanders.spotify_commander import Spotify_commander
from commanders.volume_commander import volume_commander
from commanders.cmd_commander import CMD_commander
from commanders.google_command import Google_commander
from commanders.screen_commander import screen_commander
from commanders.translate_commander import translate_commander 
import logging
from common_base import *


class Voice_command_Runner:
    def __init__(self, micr=True) -> None:
        self.listener = Mic_listener()
        self.app_container = App_container()
        self.commanders_list = [text_commander(),    # use to write to file (maybe read sometimes in the future...)
                                Spotify_commander(), # use to control spotify - for now -> next song, previous song, pause and stop (they are the same)
                                volume_commander(),  # use to control pc volume - for now -> volume up and down 
                                CMD_commander(),     # use to send CMD for practically every thing we want to do but for now only to open chrome
                                Google_commander(),  # use to search in google site using chrome
                                screen_commander(),  # use to hide the screen (with a black screen image and show the screen if hided.
                                translate_commander()# use to direct to translate word in chrome (for now using morfix)
                                                    ]
        
        self._register_commanders()
        self.print_status()
        
        
    def Run_phone_app(self) -> None:
        try:
            for text_command in self.listener.run_loop_app():
                print(text_command)
                if text_command.startswith('enable'):
                    app_to_enable = text_command.split('enable ')[1]
                    self.app_container.set_app_as_listener(app_to_enable)
                self.app_container.dispatch_command(text_command)
        except Exception as ex:
            logger.exception(ex)
            print(ex)
        
    
        
    def print_status(self):
        self.app_container.print_status()
    
    
    def Run(self, is_real_mic = True):
        """loop voice command -> get command from listen loop and dispatch the command to
        relevance commanders. 
        """
        try:
            for text_command in self.listener.listen_loop():
                print(text_command)
                if text_command.startswith('enable'):
                    app_to_enable = text_command.split('enable ')[1]
                    self.app_container.set_app_as_listener(app_to_enable)
                # logger.info(text_command)
                self.app_container.dispatch_command(text_command)
        except Exception as ex:
            logger.exception(ex)
            print(ex)

    
########################## PRIVATE FUNCTIONS #########################


    def _register_commanders(self) -> None:
        for commander in self.commanders_list:
            commander.register_self(self.app_container)
            

    def Debug_run(self):
        try:
            text_command =1
            while text_command:
                text_command = input('enter input\n')
                print(text_command)
                if text_command == 'stop':
                    break
                if text_command.startswith('enable'):
                    app_to_enable = text_command.split('enable ')[1]
                    self.app_container.set_app_as_listener(app_to_enable)
                logger.info(text_command)
                self.app_container.dispatch_command(text_command)
        except Exception as ex:
            logger.exception(ex)
            print(ex)
        
    
