from pymongo import MongoClient


class Database:
    def __init__(self, host='localhost', post=5005):
        self.__client = MongoClient(post, host)
        self.__db = self.__client['background-monitor-database']

    def update(self, pid, title):
        collection = self.__db['events']

        result = collection.find({'pid': pid, 'title': title})

        if result is None:
            pass
