from enum import IntEnum
import json
import requests
from requests.api import request
from spotify_files.spotify_data import *
import inspect    


class RESPONSE_ENUM(IntEnum):
    AUTHENTICATION_ERROR = 401
    OK = 201
    OK_NO_CONTENT = 204
    
    
class Spotify_API:
    def __init__(self):
        self.spotify_id = SPOTIFY_ID
        self.spotify_token = SPOTIFY_TOKEN
        self.refresh_token = REFRESH_TOKEN
        self.base64_id = BASE_64_ID
        self.refresh_token_id()
    
    
    def refresh_token_id(self):
        query = 'https://accounts.spotify.com/api/token'
        response = requests.post(query,
                                data={"grant_type":"refresh_token","refresh_token":self.refresh_token},
                                headers={"Authorization":"Basic " + self.base64_id})
        
        self.spotify_token = response.json()['access_token']
    
    
    def check_response_status(self, response):
        """if status fail return False. if the error is authentication error 
        try to refresh the spotify token and return False.
        
        otherwise return True"""
        if response.status_code == RESPONSE_ENUM.AUTHENTICATION_ERROR:
            self.refresh_token_id()
            return False
        if response.status_code != RESPONSE_ENUM.OK and response.status_code != RESPONSE_ENUM.OK_NO_CONTENT:
            return False
        return True
    
    
    def next_song(self):
        query = 'https://api.spotify.com/v1/me/player/next'
        response = requests.post(
        query,
        headers={
            "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        self.check_response_status(response)
                
    
    def previous_song(self):
        query = 'https://api.spotify.com/v1/me/player/previous'
        response = requests.post(
        query,
        headers={
            "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        self.check_response_status(response)
        
        
    def pause_song(self):
        query = 'https://api.spotify.com/v1/me/player/pause'
        response = requests.put(
        query,
        headers={
            "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        self.check_response_status(response)
        
    
    def play_song(self):
        device_id = self._get_id()
        query = 'https://api.spotify.com/v1/me/player/play?device_id=' + device_id
        response = requests.put(
        query,
        headers={
            "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        print(response)
        self.check_response_status(response)


    def search_song(self, song_name):
        song_uri = self._get_song_uri(song_name)
        self._play_song_uri(song_uri)
        
    
#==============================================#
#               AID FUNCTIONS                  #
#==============================================#


    def _play_song_uri(self, uri):
        print(uri)
        list_of_uri = uri.split(':') # uri list = [spotify: type: id]
        song_id = list_of_uri[2]
        query = 'https://api.spotify.com/v1/me/player/queue?uri=' + 'spotify%3Atrack%3A' + song_id
        response = requests.post(
        query,
        headers={
            "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        print(response)
        self.check_response_status(response)
        self.next_song()
    
    
    def _get_song_uri(self, song_name):
        if song_name is None:
            # TODO
            return 

        query = 'https://api.spotify.com/v1/search?q=' + song_name + '&type=track'
        response = requests.get(
        query,
        headers={
            "q":"DNA",
            "type":"track",
            "Authorization": f"Bearer {self.spotify_token}",
            }
        )
        self.check_response_status(response)
        return response.json()['tracks']["items"][0]["uri"]
        
    
    def _get_id(self):
        # TODO get the real id? 
        query = 'https://api.spotify.com/v1/me/player/devices'
        response = requests.get(
        query,
        headers={
            "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        print(response)
        try:
            devices_list = (response.json()['devices'])
            for device in devices_list:
                return (device['id'])
        except Exception as ex:
            print(ex)
            
        if self.check_response_status(response) is False:
            return DEFAULT_PC_ID
        else:
            # get the real id from the response
            return DEFAULT_PC_ID
        
