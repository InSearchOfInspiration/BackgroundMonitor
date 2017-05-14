import requests
import json


class ConnectionManager:
    # TODO delete hardcore
    __USER_NAME = 'username'
    __PASSWORD = 'ololo'

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

        r = requests.post(self.__server_url+'/login', json=data)

        if r.status_code is 200:
            r = json.loads(r.text)

            if r['access_token'] is not None:
                self.__token = r['access_token']
                self.__authorized = True
                result = True

        return result

    def post_event(self, event_json):
        if self.__authorized:
            headers = {'Authorization': 'JWT ' + self.__token}
            r = requests.post(self.__server_url+'/events/new', json=event_json, headers=headers)
        else:
            self.authorize()
