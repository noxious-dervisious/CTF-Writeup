def scoring(input_bytes):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(byte, 0) for byte in input_bytes.lower()])

def single_char_xor(input_bytes, char_value):
    output_bytes = ''
    for byte in input_bytes:
        output_bytes += chr(ord(byte) ^ char_value)
    return output_bytes

def english_attack(ciphertext):
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = scoring(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]

def exploit (ciphertext):
    return english_attack(ciphertext)['key']

def reapeting_key_xor (pt,key) :
    index= 0
    ct = '' 
    for ch in pt:
        ct += chr(ord(ch) ^ ord(key[index]))
        if index + 1 == len(key):
            index=0
        else :
            index += 1
    return ct
