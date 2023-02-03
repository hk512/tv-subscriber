import configparser

conf = configparser.ConfigParser()
conf.read("config.ini")

api_key = conf["bybit"]["api_key"]
api_secret = conf["bybit"]["api_secret"]

symbol = conf["trade"]["symbol"]
lot = float(conf["trade"]["lot"])
max_lot = float(conf["trade"]["max_lot"])

host = conf["server"]["host"]
port = conf["server"]["port"]

webhook_url = conf["slack"]["webhook_url"]
