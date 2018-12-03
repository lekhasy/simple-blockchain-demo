from kscoin.ksNonceTimestampManipulator import KSNonceTimestampManipulator
from core.block import Block
from helpers.jsonifyHelper import to_json_string
from helpers.objectHashingHelper import hash

FIXED_TARGET = 4

class KSCoin:
    def __init__(self):
        self.mempool = []
        self.nonce_timestamp_manipulator = KSNonceTimestampManipulator()
        self.target = FIXED_TARGET
        self.target_in_string = FIXED_TARGET * '0'

        # add genesys block to chain
        genesis_block = self.init_genesis_block()
        self.chain = [genesis_block]

    def init_genesis_block(self):
        genesis_data = "Some random data for genesis block!"
        genesis_block = Block(genesis_data, 1, self.target_in_string)
        nonce, timestamp = self.find_nonce(genesis_block)
        genesis_block.seal(nonce, timestamp)
        return genesis_block

    def add_transaction(self, transaction):
        self.mempool.append(transaction)

    def mine_new_block(self):
        previous_hash = self.target_in_string if len(self.chain) == 0 else hash(self.get_latest_block())
        block_data = to_json_string(self.mempool)
        block = Block(block_data, len(self.chain)+1, previous_hash)
        nonce, timestamp = self.find_nonce(block)
        block.seal(nonce, timestamp)
        self.chain.append(block)

    def is_chain_valid(self, chain):
        # validate genesis block
        if hash(chain[0])[:self.target] != self.target_in_string:
            return False

        # validate the rest
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if hash(previous_block) != block.previous_hash:
                return False
            if hash(block)[:self.target] != self.target_in_string:
                return False
            previous_block = block
            block_index += 1
        return True

    def find_nonce(self, block):
        cloned_block = block.clone()
        self.nonce_timestamp_manipulator
        while True:
            cloned_block.nonce = self.nonce_timestamp_manipulator.get_next_nonce()
            cloned_block.timestamp = self.nonce_timestamp_manipulator.get_current_timestamp()
            if hash(cloned_block)[:self.target] == self.target_in_string:
                return cloned_block.nonce, cloned_block.timestamp

    def get_latest_block(self):
        return self.chain[-1]

    def get_chain_length(self):
        return len(self.chain)

    def get_mempool(self):
        return self.mempool