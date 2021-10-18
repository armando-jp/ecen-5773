from c1p1 import hex_to_base64
from base64 import b64encode

str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"
solution = "746865206b696420646f6e277420706c6179"

def get_xor(param1: str, param2: str) -> bytes:
    """
    Takes two equal length buffers and returns their XOR combination.

    Args:
        param1: first value to be XOR'ed.
        param2: second value to be XOR'ed.

    Returns:
        The result of XOR'ing param1 and param2 as a bytes object.
    """

    b1 = bytes.fromhex(param1)
    b2 = bytes.fromhex(param2)

    result = bytes([_a ^ _b for _a, _b in zip(b1, b2)])

    return result


if __name__ == '__main__':
    result = get_xor(str1, str2)
    print(f"type: {type(result)}")
    print(f"result: {result.hex()}")
    assert result.hex() == solution
    assert type(result) == bytes