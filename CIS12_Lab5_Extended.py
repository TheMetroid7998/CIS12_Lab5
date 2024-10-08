import sys

def is_valid(part):
    """Checks if the input value is a valid integer between 0 and 255 and if the value doesn't start with 0."""
    if 0 <= int(part) <= 255 and part == str(int(part)): # was originally float(part). why?
        return True
    else:
        raise Exception(f"""
This IP address is invalid: 
Decimal values may only fall within the inclusive range of 0 - 255 and cannot start with leading zeros.
Binary values may only include '0' and '1'.
        """)

def is_valid_ip(ip):
    """Splits the ip address into a list of the 4 numbers and checks each item in the list."""
    ip = str(ip)
    split_ip = ip.split('.')

    if len(split_ip) != 4:
        raise Exception("This IP address is not valid: IP addresses can only be 4 discrete numbers in binary or decimal format.")

    for item in split_ip:
        is_valid(item)

def decimal_to_binary(n):
    """Performs basic checks before passing the decimal number to a helper function."""
    if n < 0:
        raise Exception("Negative numbers are not valid for this conversion.")
    if n == 0:
        return '0'
    return decimal_to_binary_helper(n)

def decimal_to_binary_helper(n):
    """Performs decimal to binary conversion by integer division and string concatenation."""
    if n == 0:
        return ''
    else:
        return decimal_to_binary_helper(n // 2) + str(n % 2)

def binary_to_decimal(bin_str):
    """Converts binary to decimal values. Validates the number before beginning the conversion process."""
    bin_str = str(bin_str)
    if not all(char in '01.' for char in str(bin_str)):
        raise Exception("This number is not a valid binary number; include only '0' and '1'.")
        # This currently can't be raised with the new function.
    dec_val = 0
    length = len(bin_str)
    for i in range(length):
        dec_val += int(bin_str[i]) * (2 ** (length - 1 - i))
    return dec_val #, print("Converted Successfully")

def ip_to_binary(ip):
    """Converts a set of decimal numbers into a set of binary values and concatenates them."""
    is_valid_ip(ip)
    split_ip = ip.split('.')
    bin_ip = []
    for item in split_ip:
        bin_part = decimal_to_binary(int(item))
        bin_ip.append(bin_part.zfill(8))
    # Original code (before asking ChatGPT): bin_ip += [''.join(decimal_to_binary(item)) for item in split_ip]
    return '.'.join(bin_ip)

def binary_to_ip(bin_ip):
    """Converts a set of binary values into a set of decimal numbers and concatenates them."""
    split_ip = bin_ip.split('.')
    dec_ip = []
    for item in split_ip:
        dec_part = binary_to_decimal(str(item))
        dec_ip.append(dec_part)
    dec_full = '.'.join(map(str, dec_ip))
    is_valid_ip(dec_full)
    return dec_full

def ip_convert_old(ip):
    """
    Checks for which base the ip address is in, converts it, and lists it.
    Error checking is already handled in prior functions.
    """
    if all(char in '01.' for char in str(ip)):
        print(f"The decimal representation of the binary IP address {ip} is {binary_to_ip(ip)}")
        return binary_to_ip(ip)
    else:
        print(f"The binary representation of the decimal IP address {ip} is {ip_to_binary(ip)}")
        return ip_to_binary(ip)

def manual_end():
    """Collects input to determine whether to convert another IP address."""
    desire = input("Convert another IP address?\n").upper().strip()
    if desire == 'Y':
        ip_convert()
    elif desire == 'N':
        sys.exit()
    else: # desire != 'N' or desire != 'Y':
        print("Enter only 'Y' or 'N' to indicate your preference.")
        manual_end()

def ip_input():
    """Takes the initial input and passes to another function."""
    return str(input("Enter an IP address in binary or decimal format: \n").strip())

def ip_convert():
    """Takes input, determines if it is decimal or binary, and converts it appropriately."""
    ip = ip_input()
    try:
        if all(char in '01.' for char in str(ip)) and len(ip) == 35:
            print(f"The decimal representation of the binary IP address {ip} is {binary_to_ip(ip)}")
            return binary_to_ip(ip)
        else:
            print(f"The binary representation of the decimal IP address {ip} is {ip_to_binary(ip)}")
            return ip_to_binary(ip)
    except Exception as error:
        print(error)
        ip_convert()
    finally: manual_end()

#ip_convert_old('192.168.1.1')
#ip_convert_old('11000000.10101000.00000001.00000001')
ip_convert()
