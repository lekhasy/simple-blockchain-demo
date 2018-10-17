from jsonify_helper import Serializable

class Block(Serializable):
    def __init__(self, block_data, block_index, previous_hash):
        self.index = block_index
        self.data = block_data
        self.previous_hash = previous_hash
        self.nonce = None

    def seal(self, nonce):
        self.nonce = nonce

    def clone(self):
        cloned_block = Block(self.data, self.index, self.previous_hash)
        cloned_block.nonce = self.nonce
        return cloned_block