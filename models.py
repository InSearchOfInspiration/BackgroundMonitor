from pymodm import MongoModel, fields
from config import DB_URL
from pymodm import connect

print("URL:", DB_URL)
connect(DB_URL)


class Event(MongoModel):
    name = fields.CharField(blank=False)
    pid = fields.IntegerField()
    start_date = fields.DateTimeField()
    finish_date = fields.DateTimeField()

    @property
    def id(self):
        return self._id
