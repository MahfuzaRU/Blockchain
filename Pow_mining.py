"""
Write a program in Python for mining a new block in a blockchain, and print the values of the
new block.  Blockchain + Mining

Nonce = “Number used once”

মানে এমন একটা সংখ্যা
👉 যেটা শুধু একবার ব্যবহার করা হয়
👉 Mining এর সময় বারবার change করা হয়
Data তো fixed
Previous hash fixed
Timestamp fixed

তাহলে hash change করবো কীভাবে? nonce er maddhome

Mining =
👉 Nonce বারবার change করা
👉 যতক্ষণ না valid hash পাওয়া যায়

এটাই হলো Proof of Work।
"""


import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index  #block number
        self.timestamp = time.time()    #block তৈরির সময়
        self.data = data    #block এর তথ্য (transaction)
        self.previous_hash = previous_hash  #আগের block এর has
        self.nonce = 0  #mining এর জন্য nonce
        self.hash = self.mine_block(4)

    def calculate_hash(self):
        text = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)+str(self.nonce)
        return hashlib.sha256(text.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = "0" * difficulty
        while True:
            hash_val = self.calculate_hash()
            if hash_val.startswith(prefix):
                return hash_val
            self.nonce += 1


# -------- Mining New Block --------
genesis = Block(0, "Genesis Block", "0")

mined_block = Block(1, "Transaction Data", genesis.hash)

print("New Block Mined Successfully!\n")
print("Data:", mined_block.data)
print("Nonce:", mined_block.nonce)
print("Hash:", mined_block.hash)