from base64 import b64encode

test_string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
solution="SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex_to_base64(s: str) -> bytes: 
    """
    hex -> base64

    Args:
        s: raw string representing a hex value.

    Returns:
        the raw string, s, converted to base64.
    """
    return b64encode(bytes.fromhex(s))

if __name__ == '__main__':
    result = hex_to_base64(test_string)
    print(f"type: {type(result)}")
    print(f"result: {result.decode()}")
    assert type(result) == bytes
    assert result.decode() == solution
    