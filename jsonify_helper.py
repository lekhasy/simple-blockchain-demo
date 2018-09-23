from json import JSONEncoder
import json

class Serializable:
    pass

class MyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Serializable):
            return obj.__dict__
        else:
            return super(MyEncoder, self).default(obj)

def to_json_string(data):
    return json.dumps(data, sort_keys=True, cls=MyEncoder)
