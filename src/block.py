import random
import string
from hashlib import sha256
import json


class Block:

    def __init__(self, index, prev_hash, nonce, hashed):
        self.nonce = nonce
        self.hash = hashed
        self.index = index
        letters = string.ascii_lowercase
        self.data = ''.join(random.choice(letters) for i in range(256))
        self.prev_hash = prev_hash

    def hash_block(self, by):
        while True:
            common = str(self.index) + self.prev_hash + self.data + str(self.nonce)
            current_hash = sha256(common.encode('utf-8'))
            if current_hash.hexdigest()[-4:] == "0000":
                self.hash = current_hash.hexdigest()
                break
            else:
                if by == 1:
                    self.nonce += random.randint(1, 10)

                elif by == 2:
                    self.nonce += 20
                else:
                    self.nonce += 1

    def get_json_block(self):
        dictionary = {
            'index': self.index,
            'prev_hash': self.prev_hash,
            'data': self.data,
            'hash': self.hash,
            'nonce': self.nonce
        }

        return json.dumps(dictionary)
