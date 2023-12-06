import struct
def arithmetic_encode(text, char_prob) -> float:

    high = 1.0
    low = 0.0
    for char in text:
        range = high - low
        high = low + range * char_prob[char][1]
        low = low + range * char_prob[char][0]

    return (low + high) / 2

def arithmetic_decode(encoded_number, char_prob, text_length):
    decoded_text = ''
    for _ in range(text_length):
        for char, (low, high) in char_prob.items():
            if low <= encoded_number < high:
                decoded_text += char
                encoded_number = (encoded_number - low) / (high - low)
                break

    return decoded_text

def create_uniform_probability_model(text) -> dict:
    # Count the frequency of each character in the text
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1

    total_chars = len(text)
    char_prob = {}
    current_low = 0.0

    # Calculate the probability range for each character
    for char, freq in char_freq.items():
        probability = freq / total_chars
        char_prob[char] = (current_low, current_low + probability)
        current_low += probability

    return char_prob

def float_to_binary(number, bits=64):

    # Use struct to pack the float into bytes, then format the bytes into binary
    packed = struct.pack('d' if bits == 64 else 'f', number)
    binary_format = ''.join(f'{byte:08b}' for byte in packed)

    return binary_format

def binary_to_float(binary_data, bits=64):

    # Convert the binary string to bytes
    byte_array = int(binary_data, 2).to_bytes(bits // 8, byteorder='big')

    # Unpack the bytes to a float
    number = struct.unpack('d' if bits == 64 else 'f', byte_array)[0]
    return number
