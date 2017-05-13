import requests
import json


class ConnectionManager:
    __USER_NAME = ''
    __PASSWORD = ''

    def __init__(self, server_url):
        self.__server_url = server_url
        self.__token = None
        self.__authorized = False

    def authorize(self) -> bool:
        result = False

        data = json.dumps({
            'username': self.__USER_NAME,
            'password': self.__PASSWORD
        })
        header = {'Accept': 'application/json'}

        r = requests.post(self.__server_url+'/login/', data=data, header=header)
        r = json.loads(r.text)

        if r['token'] is not None:
            self.__token = r['token']
            self.__authorized = True
            result = True

        return result

    def post_event(self, event):
        if self.__authorized:
            data = json.dumps(event)
            header = {'Accept': 'application/json'}
            r = requests.post(self.__server_url, data=data, header=header)
        else:
            self.authorize()
