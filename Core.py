#This file is for handle the functions from Utils
#Providing the functions to telegram's api
import Utils
import json
import requests

class Core:
    def Config(self):
        configFile = Utils.Utils.LoadConfig(self)
        telegram_token = configFile['token']
        return telegram_token
    
    def LoadAPI(self):
        token = self.Config
        LoadJSON = json.loads(requests.get(f'https://api.telegram.org/bot{token}'))
        #Pulling