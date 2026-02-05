import string
def alt_caps(original_string):
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """
    new_string = ""
    original_string = "alternating capitalization"
    runtime=-1
    for i in original_string:
        if runtime%2 == 0:
            newCharacter=i.upper()
        else:
            newCharacter=i
        new_string += newCharacter
        runtime+=1
    return new_string
print(alt_caps("Alternating Capitalization"))