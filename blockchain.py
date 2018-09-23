import hashlib
from block import Block
from jsonify_helper import to_json_string

class Blockchain:
    def __init__(self, target):
        # preparing stuffs
        self.chain = []
        self.target = target
        self.target_in_string = self.target * '0'

        # add genesys block to chain
        self.create_block("Some random data for genesis block!")

    def create_block(self, data):
        previous_hash = self.target_in_string if len(self.chain) == 0 else self.hash(
            self.get_latest_block())

        block = Block(data, len(self.chain)+1, previous_hash)
        proof_of_work = self.find_proof_of_work(block)
        block.seal(proof_of_work)
        self.chain.append(block)

    def find_proof_of_work(self, block):
        cloned_block = block.clone()
        new_proof = 1
        check_proof = False
        while check_proof is False:
            cloned_block.proof_of_work = new_proof
            if self.hash(cloned_block)[:self.target] == self.target_in_string:
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, hashedObject):
        block_in_string = to_json_string(hashedObject).encode()
        return hashlib.sha256(block_in_string).hexdigest()

    def is_chain_valid(self, chain):
        #validate genesis block
        if self.hash(chain[0])[:self.target] != self.target_in_string:
            return False

        #validate the rest
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if self.hash(previous_block) != block.previous_hash:
                return False
            if self.hash(block)[:self.target] != self.target_in_string:
                return False
            previous_block = block
            block_index += 1
        return True

    def get_latest_block(self):
        return self.chain[-1]

    def get_chain_length(self):
        return len(self.chain)