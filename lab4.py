def calculate_parity_bits(data):
    n = len(data)
    m = 0
    while 2 ** m < n + m + 1:
        m += 1
    parity_bits = [0] * m

    j = 0
    for i in range(1, n + m + 1):
        if i == 2 ** j:
            parity_bits[j] = calculate_parity(data, i)
            j += 1
    return parity_bits

def calculate_parity(data, parity_index):
    count = 0
    for i in range(len(data)):
        if data[i] == '1' and is_set(i + 1, parity_index):
            count += 1
    return count % 2

def is_set(bit, position):
    return bit & (1 << (position - 1))

def encode_data(data):
    n = len(data)
    m = 0
    while 2 ** m < n + m + 1:
        m += 1

    j = 0
    encoded_data = []
    for i in range(1, n + m + 1):
        if i == 2 ** j:
            encoded_data.append(0)
            j += 1
        else:
            if j < n:
                encoded_data.append(int(data[j]))
                j += 1
            else:
                encoded_data.append(0)

    parity_bits = calculate_parity_bits(encoded_data)
    for i in range(m):
        encoded_data[2 ** i - 1] = parity_bits[i]

    return ''.join(map(str, encoded_data))

def flip_bit(bit):
    return '0' if bit == '1' else '1'

def detect_error(encoded_data):
    m = 0
    while 2 ** m < len(encoded_data):
        m += 1

    error_position = 0
    for i in range(m):
        parity_index = 2 ** i
        calculated_parity = calculate_parity(encoded_data, parity_index)
        if calculated_parity != int(encoded_data[parity_index - 1]):
            error_position += parity_index

    return error_position

def correct_error(encoded_data):
    error_position = detect_error(encoded_data)
    if error_position != 0:
        encoded_data = list(encoded_data)
        encoded_data[error_position - 1] = flip_bit(encoded_data[error_position - 1])
        return ''.join(encoded_data)
    else:
        return encoded_data

def decode_data(encoded_data):
    m = 0
    while 2 ** m < len(encoded_data):
        m += 1

    decoded_data = []
    j = 0
    for i in range(1, len(encoded_data) + 1):
        if i == 2 ** j:
            j += 1
        else:
            decoded_data.append(encoded_data[i - 1])

    return ''.join(decoded_data)

# Example usage:
data = "1101"  # Input data
encoded_data = encode_data(data)
print("Encoded data:", encoded_data)

# Simulate an error by flipping one bit
error_position = 3
encoded_data = list(encoded_data)
encoded_data[error_position - 1] = flip_bit(encoded_data[error_position - 1])
encoded_data = ''.join(encoded_data)
print("Data with error:", encoded_data)
# Correct the error
corrected_data = correct_error(encoded_data)
print("Corrected data:", corrected_data)

# Decode the corrected data
decoded_data = decode_data(corrected_data)
print("Decoded data:", decoded_data)
