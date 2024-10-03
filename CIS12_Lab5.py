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
    ip = str(ip)
    split_ip = ip.split('.')

    if len(split_ip) != 4:
        print("This IP Address is not valid: IP Address is not the correct length.")
        return False

    for item in split_ip:
        if not is_valid(item):
            print("This IP Address is not valid: IP Address values are invalid.")
            return False
    #print("This IP Address is valid.")
    return True

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

def binary_to_decimal(bin_str):
    """Converts binary to decimal values. Validates the number before beginning the conversion process."""
    bin_str = str(bin_str)
    if not all(char in '01' for char in str(bin_str)):
        return "This number is not a valid binary number."
    dec_val = 0
    length = len(bin_str)
    for i in range(length):
        dec_val += int(bin_str[i]) * (2 ** (length - 1 - i))
    return dec_val

def ip_to_binary(ip):
    if is_valid_ip(ip):
        # print("IP Address is valid and ready for conversion.")
        pass
    else:
        return "Invalid IP Addresses cannot be converted."
    split_ip = ip.split('.')
    bin_ip = []
    for item in split_ip:
        bin_part = decimal_to_binary(int(item))
        bin_ip.append(bin_part.zfill(8))
#   Original Code (Before asking ChatGPT): bin_ip += [''.join(decimal_to_binary(item)) for item in split_ip]
    return '.'.join(bin_ip)

def binary_to_ip(bin_ip):
    split_ip = bin_ip.split('.')
    dec_ip = []
    for item in split_ip:
        dec_part = binary_to_decimal(str(item))
        dec_ip.append(dec_part)
    dec_full = '.'.join(map(str, dec_ip))
    if is_valid_ip(dec_full):
        return dec_full
    else:
        return "Invalid IP Addresses cannot be converted."

def ip_convert(ip):
    if all(char in '01.' for char in str(ip)):
        print(f"The decimal representation of the binary IP address {ip} is {binary_to_ip(ip)}")
        return binary_to_ip(ip)
    else:
        print(f"The binary representation of the decimal IP address {ip} is {ip_to_binary(ip)}")
        return ip_to_binary(ip)

ip_convert('192.168.1.1')
ip_convert('11000000.10101000.00000001.00000001')
