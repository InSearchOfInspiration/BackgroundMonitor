from pymodm import MongoModel, fields
from config import DB_URL
from pymodm import connect
import json

print("URL:", DB_URL)
connect(DB_URL)


class Event(MongoModel):
    name = fields.CharField(blank=False)
    pid = fields.IntegerField()
    start_date = fields.DateTimeField()
    finish_date = fields.DateTimeField()
    category = fields.DictField()

    def json_representation(self):
        result = {}
        if 'id' in self.category \
                and 'name' in self.category:

            result['category'] = self.category

        result['start_date'] = self.start_date.isoformat()
        result['finish_date'] = self.finish_date.isoformat()
        result['name'] = self.name
        result['source_type'] = 0

        return json.dumps(result)

    @property
    def id(self):
        return self._id
