import time
import models


class Database:
    def __init__(self):
        self.__last_updated_event_id = None

    def update(self, pid, name):
        events = models.Event.objects.raw({'pid': pid, 'name': name})

        if events.count() is not 0:
            for event in events:
                if event.id == self.__last_updated_event_id:
                    event.finish_date = time.time()
                    event.save()
                    break
                else:
                    self.__create_event(pid, name)
        else:
            self.__create_event(pid, name)

    def __create_event(self, pid, name):
        time_now = time.time()
        event = models.Event(name, pid, time_now, time_now).save()

        self.__last_updated_event_id = event.id
