import hashlib
import hmac

def hash_password(password: str) -> str:
    # Convert to bytes and hash using SHA-256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(stored_hash: str, input_password: str) -> bool:
    # Secure comparison to prevent timing attacks
    input_hash = hash_password(input_password)
    return hmac.compare_digest(stored_hash, input_hash)

# Example usage
password = "MySecurePass123!"
stored_hash = hash_password(password)

print("Stored Hash:", stored_hash)

# Correct input
print("Verify (correct):", verify_password(stored_hash, "MySecurePass123!"))

# Incorrect input
print("Verify (wrong):", verify_password(stored_hash, "WrongPass"))
