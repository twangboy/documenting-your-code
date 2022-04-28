import random
import string
from typing import Optional, Iterable


def generate_password(chars: int, punctuation: bool, invalid_chars: Optional[Iterable[str]] = None) -> str:
    """
    Generate a random password with optional punctuation and avoiding specified invalid characters.

    Args:
        chars (int): The number of characters the password should contain
        punctuation (bool): Include punctuation characters if True
        invalid_chars (list, None): List of invalid characters, or None

    Returns:
        str: A randomized password
    """
    valid_chars = string.ascii_letters + string.digits

    # include punctuation of passed
    if punctuation:
        valid_chars += string.punctuation

    # specify invalid characters
    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    # Use random to generate a bunch of random characters using valid_characters
    password_chars = random.choices(valid_chars, k=chars)
    # Not sure of the purpose of this
    password = "".join(char for char in password_chars)

    return password
