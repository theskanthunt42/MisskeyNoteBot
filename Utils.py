import json
import requests


class Utils:
    def AddToken(self, uid, site, token):
        with open('TokenLib.json', 'r') as f:
            loaded_json = json.load(f.read())
        if uid in loaded_json:
            return True, 'You already added a token to this bot, Please delete using /deltoken'
        else:
            loaded_json[uid] = [site, token]
            save_json = json.dumps(loaded_json)
            with open('TokenLib.json', 'w') as f:
                f.write(save_json)
            return True, 'Successfully add token.'

    def DeleteToken(self, uid):
        with open('TokenLib.json', 'r') as f:
            loaded_json = json.load(f.read())
        if uid in loaded_json:
            loaded_json.pop(uid)
            save_json = json.dumps(loaded_json)
            with open('TokenLib.json', 'w') as f:
                f.write(save_json)
            return True, 'Successfully delete your token.'
        else:
            return False, 'Token is not added to this bot yet! Please add by using /addtoken'

    def CheckToken(self, uid):
        with open('TokenLib.json', 'r') as f:
            loaded_json = json.loads(f.read())
            if uid in loaded_json:
                return True, loaded_json[uid][0], loaded_json[uid][1]
            else:
                return False, '', ''

    def ReadToken(self, uid):
        site, token_exist, token = self.CheckToken(uid)
        if token_exist:
            return site, token
        else:
            return None
# This function is use to send the note
# Will add renote(And quote) later

    def SendNote(self, text, visibility, uid):
        site, token = self.ReadToken(uid)
        if token == None:
            return False, 'No token.'
        else:
            pass
        payload = '{"i":"{}", "text":"{text}", "visibility":"{visibility}"}'.format(
            token, text, visibility)  # Add other functions like renote here
        send_the_note = requests.post(site+'/api/notes/create', data=payload)
        if send_the_note.status_code != 200:
            return False, 'Failed to send note', send_the_note.status_code
        else:
            pass
            return send_the_note.text

    def LoadConfig(self):
        with open('config.json', 'r') as f:
            configDict = json.load(f.read())
        return configDict