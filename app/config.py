import json

class Config:
    def __init__(self):
        with open("appsettings.json") as f:
            config = json.load(f)
            self.SECRET_KEY = config["SECRET_KEY"]
            self.DB_PATH = config["DB_PATH"]
