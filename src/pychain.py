from random import randint
import hashlib
import json
import time

class pyChain:
    def __init__(self):
        self.chain = []
        self.chain.append(self.Block(0,"0"*64,None,0,0,"genesis"))
        self.difficulty = 3;

    def Block(self, index, hash, prev_hash, pow, nonce, data):
        return {
            "index": index,
            "timestamp": self.Timestamp(),
            "hash": hash,
            "prev_hash": prev_hash,
            "pow": pow,
            "nonce": nonce,
            "data": data
        }

    def Timestamp(self):
        return int(time.time())
