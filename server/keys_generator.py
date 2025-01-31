import random
import hashlib


def generate_key(user_id: int) -> str:
    key_seed = f"{user_id}{random.randint(1, 999999)}"
    h = hashlib.new("sha256")
    h.update(bytes(key_seed, "utf-8"))
    return h.hexdigest()
