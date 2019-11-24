import requests


class HTTP:

    @staticmethod
    def get(url, json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if json else ''
        return r.json() if json else r.text
