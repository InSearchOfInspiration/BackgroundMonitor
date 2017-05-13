from background_monitor import BackgroundMonitor
from database import Database

if __name__ == '__main__':
    database = Database()

    background_monitor = BackgroundMonitor(database)
    background_monitor.run()
