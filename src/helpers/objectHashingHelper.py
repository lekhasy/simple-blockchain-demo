import hashlib
from helpers.jsonifyHelper import to_json_string

def hash(hashedObject):
        block_in_string = to_json_string(hashedObject).encode()
        return hashlib.sha256(block_in_string).hexdigest()