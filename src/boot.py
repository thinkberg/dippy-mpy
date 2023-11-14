import json

credentials = {}

with open("config.json", "r") as f:
    credentials = json.load(f)
