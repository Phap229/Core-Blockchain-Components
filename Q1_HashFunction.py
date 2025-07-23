import hashlib
import random
import string

# Avalanche Effect
input_str = input("Enter a string: ")
hash_original = hashlib.sha256(input_str.encode()).hexdigest()
print(f"Original Input: {input_str}")
print(f"Original Hash: {hash_original}")

# Modify input slightly to show avalanche effect
modified_str = input_str + "a"  
hash_modified = hashlib.sha256(modified_str.encode()).hexdigest()
print(f"Modified Input: {modified_str}")
print(f"Modified Hash: {hash_modified}")

# Pre-image Resistance
target_hash = hashlib.sha256("hello".encode()).hexdigest()
print(f"\nTarget Hash to Find Pre-image For: {target_hash}")
attempts = 0
max_attempts = 1000000
found = False

# Try to find a string whose SHA-256 hash matches the target hash
for _ in range(max_attempts):
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # Generate random string
    current_hash = hashlib.sha256(random_str.encode()).hexdigest()
    attempts += 1
    if current_hash == target_hash:
        found = True
        print(f"Pre-image found: {random_str}")
        break

if not found:
    print(f"No pre-image found after {attempts} attempts.")