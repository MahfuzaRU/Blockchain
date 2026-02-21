'''
Write a Python program using a Merkle Tree to determine whether a given data block has been tampered with or not. 

'''

import hashlib

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()


# ---------------------------
# Build Merkle Tree
# ---------------------------
def build_merkle_root(data_blocks):
    level = [h(x) for x in data_blocks]

    while len(level) > 1:
        new_level = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i+1] if i+1 < len(level) else left
            new_level.append(h(left + right))
        level = new_level

    return level[0]  # Merkle Root


# ---------------------------
# Original Data
# ---------------------------
data = ["Tx1", "Tx2", "Tx3", "Tx4"]

original_root = build_merkle_root(data)

print("Original Merkle Root:", original_root)


# ---------------------------
# Simulate Tampering
# ---------------------------
tampered_data = ["Tx1", "Tx2", "Tx3", "Tx4"]

tampered_root = build_merkle_root(tampered_data)

print("Tampered Merkle Root:", tampered_root)


# ---------------------------
# Check Integrity
# ---------------------------
if original_root == tampered_root:
    print("\nData is NOT tampered.")
else:
    print("\n⚠️ Data has been TAMPERED!")