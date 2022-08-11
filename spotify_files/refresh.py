from urllib import response
import requests
import json 


class refresh:
    def __init__(self):
        self.refresh_token = 'AQDLAcFuDxLazl6pThUJyG75g5LlgMGEVah8Z-EjVqYcNJYdlJX48Lpd8tYGTCHil3BpUXIDqdXSKSOcLDmprbwO3goR63_kr9ZitqfYeDBC8xdklboVYpOvg_faLNLHqn0'
        self.base64 = 'ZDNmODAxZTFhZmM5NDEwYjlhY2QzYTFlNjg2MGRhYTI6MjU5MmJmNGYxYzMyNDJhY2JkNzJmZTViZmNjMGNiNjc='
        
        
    def refresh(self):
        query = 'https://accounts.spotify.com/api/token'
        response = requests.post(query,
                                data={"grant_type":"refresh_token","refresh_token":self.refresh_token},
                                headers={"Authorization":"Basic " + self.base64})
        
        new_token = response.json()['access_token']
        
ref = refresh()
ref.refresh()