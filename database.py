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
        if result is not None:
            pass

        if name is not None and name.replace(' ', '') is not '':
            time_now = time.time()
            event = models.Event(name, pid, time_now, time_now).save()

            self.__last_updated_event_id = event.id
            self.__connection_manager.post_event(event.json_representation())
