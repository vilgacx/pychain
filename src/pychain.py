import hashlib
import json
import time

class pyChain:
    def __init__(self):
        self.chain = [] 
        self.nodes = []
        self.chain_length = 0
        self.difficulty = max(3,min((len(self.nodes)+1)//3,7));
        self.Mine(0,"genesis")

    def Block(self, index, hash, prev_hash, pow, nonce, data):
        return {
            "index": index,
            "timestamp": self.Timestamp(),
            "hash": hash,
            "difficulty": self.difficulty,
            "prev_hash": prev_hash,
            "pow": pow,
            "transactions": [],
            "nonce": nonce,
            "data": data
        }

    def Mine(self, nonce, data):
        block = {}
        if self.chain_length > 0:
            prev_block = self.chain[-1]

            index = len(self.chain)
            pow = self.PoW(index,prev_block["pow"],nonce,data)
            prev_hash = prev_block["hash"]

            block = self.Block(index,"",prev_hash, pow, nonce, data)
            block["hash"] = self.Hash(block);
        else:
            block = self.Block(0, "", None, 0, nonce, data)
            block["hash"] = self.Hash(block)

        self.chain.append(block)
        self.chain_length += 1

    def PoW(self, index, prev_pow, nonce, data):
        pow = 1
        solve = "0"*self.difficulty;

        while True:
            digest = self.toDigest(index,pow,prev_pow,nonce,data)
            hashval = hashlib.sha256(digest).hexdigest()

            if hashval[:self.difficulty] == solve:
                break
            else:
                pow += 1

        return pow
 
    def toDigest(self,index,pow,prev_pow,nonce,data):
        return (str((pow+prev_pow+nonce**2)+index)+data).encode()

    def Hash(self,val):
        hash = hashlib.sha256(json.dumps(val, sort_keys=True).encode()).hexdigest()
        return hash

    def Timestamp(self):
        return int(time.time())
