from c1p1 import hex_to_base64


from c1p2 import get_xor

encrypted_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def count_characters(text: str) -> int:
    """
    Returns a count of alphabetical characters in a string.

    Args:
        text: a string you want to know the number of alphabetic characters.

    Returns: an integer representing the number of alphabetic characters in a string.
    """
    filtered = [c.lower() for c in text if c.isalpha()]
    return(len(filtered))

def single_byte_xor_cipher(encrypted_str_hex: str) -> tuple:
    """
    Deciphers an encrypted string which is hex encoded and determines the key.

    Args:
        encrypted_str_hex: the hex encoded and encrypted string which you would
                           to know the key and decoded solution.
    
    Returns: a tuple (decrypted_message, key, score)
    """
    encrypted_str_b = bytes.fromhex(encrypted_str_hex)

    result = (0x0, 0x0, 0x0) # (decrypted_message, key, score)

    # iterate through all ascii characters
    for ch in range(0, 128):
        # create a bytearray as big as encrypted_str, initialized to ch
        char_arr = bytearray([ch] * len(encrypted_str_b)) 
        # XOR the two bytearrays
        decrypted_message = get_xor(char_arr.hex(), encrypted_str_b.hex())
        score = count_characters(decrypted_message.decode('utf-8'))
        key = ch

        # print(f"decrypted_message: {decrypted_message.decode('utf-8')}, key: {chr(key)}, score: {score}")

        if score > result[2]:
            result = (decrypted_message, key, score)

    return result
    

if __name__ == "__main__":
    result = single_byte_xor_cipher(encrypted_str)
    print(result[0].decode('utf-8'))
    print(f"key: {chr(result[1])}")
    # print(f"score: {result[2]}")