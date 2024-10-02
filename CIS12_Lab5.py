#import math

"""
def is_valid_range(part):
    if 0 <= part <= 255:
        return True
    else:
        return False

def is_valid_format(part):
    if part == str(int("part")):
        return True
    else:
        return False

def validity_check_beta(part):
    is_valid_range(part)
    print(is_valid_range(part))
    is_valid_format(part)
    print(is_valid_format(part))
"""

def is_valid(part):
    """Checks for two conditions: if the input value is a valid integer between 0 and 255 and if the value doesn't start with 0"""
    if 0 <= float(part) <= 255 and part == str(int(part)):
    # alternatively, you could check 'part'[0] == 0, but this comes with the drawback of not accepting a lone 0
    #    print(f"{part} is a valid input for 2 checks.") # use for debugging
        return True
    else:
    #    print(f"{part} failed one or both checks; it must be a number between 0-255 and cannot start with leading zeros.") # use for debugging
        return False

def is_valid_ip(ip):
    """Splits the ip address into a list of the 4 numbers and checks each item in the list."""
    split_ip = ip.split('.')

    if len(split_ip) != 4:
        print("This IP Address is not valid: IP Address is not the correct length.")
        return

    for item in split_ip:
        if not is_valid(item):
            print("This IP Address is not valid: IP Address values are invalid.")
            return
    print("This IP Address is valid.")
    """
    Original that I came up with, not sure how to integrate the checks with this version.
    n = 0
    while n < len(split_ip):
        is_valid(split_ip[n])
        n = n + 1
    """

def decimal_to_binary(n):
    """Performs basic checks before passing the decimal number to a helper function."""
    if n < 0:
        return "Negative numbers are not valid for this conversion."
    if n == 0:
        return '0'
    return decimal_to_binary_helper(n)

def decimal_to_binary_helper(n):
    """Performs decimal to binary conversion by integer division and string concatenation."""
    if n == 0:
        return ''
    else:
        return decimal_to_binary_helper(n // 2) + str(n % 2)

def binary_to_decimal(binary_str):
    """Converts binary to decimal values. Validates the number before beginning the conversion process."""
    binary_str = str(binary_str)
    if not all(char in '01' for char in str(binary_str)):
        return "This number is not a valid binary number."
    decimal_val = 0
    length = len(binary_str)
    for i in range(length):
        decimal_val += int(binary_str[i]) * (2 ** (length - 1 - i))
    return decimal_val

