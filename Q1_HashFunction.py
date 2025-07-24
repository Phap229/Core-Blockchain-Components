import hashlib
import random
import string

def hash_string(s):
    # Using SHA-256
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def hamming_distance(s1, s2):
    # Calculate Hamming distance between two hex strings
    # Use Chat GPT for helping implement hamming
    b1 = bin(int(s1, 16))[2:].zfill(256)
    b2 = bin(int(s2, 16))[2:].zfill(256)
    return sum(c1 != c2 for c1, c2 in zip(b1, b2))

def minimal_change(s):
    # Change the first character (if possible), else append 'a'
    if not s:
        return 'a'
    c = s[0]
    # Change to a different character
    new_c = chr((ord(c) + 1) % 128)
    return new_c + s[1:]

def demonstrate_avalanche():
    user_input = input("Enter a string: ")
    original_hash = hash_string(user_input)
    modified_input = minimal_change(user_input)
    modified_hash = hash_string(modified_input)
    print(f"\nOriginal input: {user_input}")
    print(f"Original hash: {original_hash}")
    print(f"\nModified input: {modified_input}")
    print(f"Modified hash: {modified_hash}")
    dist = hamming_distance(original_hash, modified_hash)
    print(f"\nHamming distance between hashes: {dist} bits out of 256")

def preimage_attack_demo():
    print("\n--- Pre-image Resistance Demonstration ---")
    target_string = "blockchain"
    target_hash = hash_string(target_string)
    print(f"Target string: {target_string}")
    print(f"Target hash: {target_hash}")
    attempts = 0
    found = False
    max_attempts = 100000  # Limit for demonstration
    for _ in range(max_attempts):
        # Generate a random 8-character string
        candidate = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        candidate_hash = hash_string(candidate)
        attempts += 1
        if candidate_hash == target_hash:
            found = True
            print(f"Pre-image found! String: {candidate}")
            break
    if not found:
        print(f"No pre-image found in {attempts} attempts.")
    else:
        print(f"Pre-image found in {attempts} attempts.")

if __name__ == "__main__":
    demonstrate_avalanche()
    preimage_attack_demo()
