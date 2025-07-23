
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generate public-private key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,  
    key_size=2048 
)
public_key = private_key.public_key()  # Derive public key

# Serialize public key for display 
pub_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()
print(f"Public Key:\n{pub_pem}")

# Sign a message
message = input("Input String:")  
message_bytes = message.encode()  # Convert message to bytes for signing

# Sign the message using the private key and PSS padding
signature = private_key.sign(
    message_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),  # Mask generation function
        salt_length=padding.PSS.MAX_LENGTH  # Maximum salt for security
    ),
    hashes.SHA256()  # Hash algorithm for the signature
)
print(f"Message: {message}")
print(f"Signature: {signature.hex()}")  

# Verify the signature
try:
    # Verify the signature using the public key
    public_key.verify(
        signature,
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except:
    print("Signature is invalid.")
