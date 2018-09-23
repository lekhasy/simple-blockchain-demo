from jsonify_helper import Serializable

class Block(Serializable):
    def __init__(self, block_data, block_index, previous_hash):
        self.index = block_index
        self.data = block_data
        self.previous_hash = previous_hash
        self.proof_of_work = None

    def seal(self, proof_of_work):
        self.proof_of_work = proof_of_work

    def clone(self):
        cloned_block = Block(self.data, self.index, self.previous_hash)
        cloned_block.proof_of_work = self.proof_of_work
        return cloned_block