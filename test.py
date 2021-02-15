import json
#with open('TokenLib.json', 'r') as f:
#    LoadedJSON = json.loads(f.read())
#print(LoadedJSON)
#LoadedJSON[''] = ['', '']
#SaveJSON = json.dumps(LoadedJSON)
#with open('TokenLib.json', 'w') as f:
#    f.write(SaveJSON)

with open('TokenLib.json', 'r') as f:
    LoadedJSON = json.loads(f.read())
LoadedJSON.pop('')
print(LoadedJSON)
