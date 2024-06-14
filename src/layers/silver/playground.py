import json

if __name__ == '__main__':
    filepath = '/home/john/sportsbook-scrapers/src/layers/bronze/data/dk-doubles_20240424124008.json'
    with open(filepath, 'r') as file:
        data = json.load(file)
    for i,key in enumerate(data.keys()):
        print(key)
