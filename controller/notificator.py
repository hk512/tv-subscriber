import json

import requests


class Notificator(object):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def notify(self, text):
        payload = {
            "username": f"tv-subscriber",
            "attachments": [
                {
                    "text": text,
                }
            ],
        }
        res = requests.post(url=self.webhook_url, data=json.dumps(payload))
        return res
