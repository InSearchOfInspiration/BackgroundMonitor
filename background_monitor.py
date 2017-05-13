from subprocess import PIPE, Popen
import time
from threading import Timer


class BackgroundMonitor:
    __PROCESS_PING_INTERVAL = 1.0

    def __init__(self, db):
        self.__db = db
        self.__timer = Timer(self.__PROCESS_PING_INTERVAL, self.__update)
        self.__root_check = ''
        self.__stopped = False

    def run(self):
        print('run')
        self.__timer.start()

    def stop(self):
        self.__stopped = True

    def __update(self):
        print('__update')
        delta = self.__ping()
        # self.__stopped = True
        if not self.__stopped:
            if delta > self.__PROCESS_PING_INTERVAL:
                self.__timer = Timer(0.0, self.__update).start()
            else:
                self.__timer = Timer(self.__PROCESS_PING_INTERVAL-delta, self.__update).start()

    def __ping(self):
        print('__ping')
        time_before_ping = time.time()
        root = Popen(['xprop', '-root'], stdout=PIPE)
        title = ''
        pid = None

        if root.stdout != self.__root_check:
            self.__root_check = root.stdout

            for i in root.stdout:
                if '_NET_ACTIVE_WINDOW(WINDOW):'.encode('utf-8') in i:
                    id_ = i.split()[4]
                    id_w = Popen(['xprop', '-id', id_], stdout=PIPE)

            for j in id_w.stdout:
                if 'WM_ICON_NAME(STRING)'.encode('utf-8') in j:
                    if title != j.split()[2]:
                        title = j.split()[2].decode('utf-8')[1:]

                if '_NET_WM_PID(CARDINAL)'.encode('utf-8') in j:
                    pid = j.split()[2]

        if pid is not 0 and title is not None:
            self.__db.update(int(pid), str(title))

        return time_before_ping - time.time()
