import json

with open('test.json', 'r+') as f:
    data = json.load(f)
    data['12']["test"] = "test"
    f.seek(0)        
    json.dump(data, f, indent=4)
    f.truncate()
