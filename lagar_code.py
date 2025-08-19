import base64
from fractions import Fraction


def form_secret(raw_secret: str, mode: str = 's') -> tuple[str, Fraction]:
    """The function that forms the raw secret to the dec one.
    @param mode: s for string, n for numbers, b for base64 string."""
    secret: int = 0

    if mode == 'n':
        secret = int(raw_secret)

    elif mode == 'b':
        # If raw_secret is a base64 code
        secret = int.from_bytes(base64.b64decode(raw_secret), 'big')
    else:
        # Or just process it like a simple string
        secret = int.from_bytes(base64.b64encode(raw_secret.encode()), 'big')

    return (mode, Fraction(secret))


def retrive_secret(secret: Fraction, mode: str):
    """The function that retrives the dec secret to the raw one.
    @param mode: s for string, n for numbers, b for base64 string."""

    raw_secret: str = ''

    if mode == 'n':
        raw_secret = str(secret.numerator)
    elif mode == 'b':
        raw_secret = base64.b64encode(secret.numerator.to_bytes(
            secret.numerator.bit_length() + 7 // 8, 'big')).decode()
    else:
        raw_secret = base64.b64decode(secret.numerator.to_bytes(
            secret.numerator.bit_length() + 7 // 8, 'big')).decode()

    return raw_secret
