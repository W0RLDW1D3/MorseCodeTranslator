MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def encode_morse_code(message):
    encoded_message = ''
    for char in message:
        if char.upper() in MORSE_CODE_DICT:
            encoded_message += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            encoded_message += char
    return encoded_message

def decode_morse_code(message):
    decoded_message = ''
    morse_code_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    for code in message.split(' '):
        if code in morse_code_dict:
            decoded_message += morse_code_dict[code]
        else:
            decoded_message += code
    return decoded_message

# Example usage
message = 'HELLO WORLD'

encoded_message = encode_morse_code(message)
print(f'Encoded Message: {encoded_message}')

decoded_message = decode_morse_code(encoded_message)
print(f'Decoded Message: {decoded_message}')
