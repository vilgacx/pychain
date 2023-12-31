import hashlib
import json
import time

class pyChain:
    def __init__(self):
        self.chain = [] 
        self.nodes = []
        self.difficulty = max(3,3*(len(self.nodes)+1)//4);
        self.chain.append(self.Block(0,"0"*64,None,0,0,"genesis"))

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
        prev_block = self.chain[-1]

        index = len(self.chain)
        pow = self.PoW(index,prev_block["pow"],nonce,data)
        prev_hash = prev_block["hash"]

        block = self.Block(index,"",prev_hash, pow, nonce, data)
        block["hash"] = self.Hash(block);

        self.chain.append(block)
    
    def PoW(self, index, prev_pow, nonce, data):
        pow = 1
        solve = "0"*self.difficulty;

        while True:
            digest = (str((pow+prev_pow+nonce**2)+index)+data).encode()
            hashval = hashlib.sha256(digest).hexdigest()

            if hashval[:self.difficulty] == solve:
                break
            else:
                pow += 1

        return pow


    def Hash(self,val):
        hash = hashlib.sha256(json.dumps(val, sort_keys=True).encode()).hexdigest()
        return hash

    def Timestamp(self):
        return int(time.time())
