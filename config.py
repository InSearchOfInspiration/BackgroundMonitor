import os

DB_URL = os.environ.get('DB_URL')
if not DB_URL:
    DB_URL = 'mongodb://localhost:27017/background-monitor-database'

SERVER_URL = os.environ.get('SERVER_URL')
if not SERVER_URL:
    SERVER_URL = 'http://10.55.42.159:5000'
