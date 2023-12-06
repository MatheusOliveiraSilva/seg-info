import random

def generate_stream_cipher_key(length):
    return ''.join(random.choice('01') for _ in range(length))

def xor_operation(binary_data, key):
    return ''.join('1' if bit != key_bit else '0' for bit, key_bit in zip(binary_data, key))

