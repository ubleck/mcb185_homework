import math

def char_to_prob(char):
    q = ord(char) - 33
    if q < 0: return None
    return 10**(-q / 10)


def prob_to_char(p):
    q = -10 * math.log10(p)
    ascii_val = round(q) + 33
    if q <= 0 or q >= 126: return None
    return chr(ascii_val)
print(char_to_prob('B'))
print(prob_to_char(0.095))