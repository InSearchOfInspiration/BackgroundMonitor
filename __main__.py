from background_monitor import BackgroundMonitor
from database import Database
from connection_manager import ConnectionManager
from config import SERVER_URL


if __name__ == '__main__':
    connection_manager = ConnectionManager(SERVER_URL)
    connection_manager.authorize()
    database = Database(connection_manager)

    background_monitor = BackgroundMonitor(database)
    background_monitor.run()
