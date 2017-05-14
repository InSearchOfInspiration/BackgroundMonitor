import time
import models
from process_analyzer import ProcessAnalyzer


class Database:
    def __init__(self, connection_manager):
        self.__last_updated_event_id = None
        self.__connection_manager = connection_manager

    def update(self, pid, name):
        events = models.Event.objects.raw({'pid': pid, 'name': name})

        if events.count() is not 0:
            result = False
            for event in events:
                if event.id == self.__last_updated_event_id:
                    event.finish_date = time.time()
                    event.save()
                    result = True
                    break
            if not result:
                self.__create_event(pid, name)
        else:
            self.__create_event(pid, name)

    def __create_event(self, pid, name):
        result = ProcessAnalyzer.analyze(pid)
        category_id = None

        if result is not None and 'name' in result:
            category_id = self.__connection_manager.get_category(result['name'])

        if name is not None and name.replace(' ', '') is not '':
            time_now = time.time()
            event = models.Event(name, pid, time_now, time_now)

            if category_id is not None:
                event.category = {'name': result['name'], 'id': category_id}

            event.save()
            self.__last_updated_event_id = event.id
            self.__connection_manager.post_event(event.json_representation())
