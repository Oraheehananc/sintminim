# Example byte sequence with null characters
locale_bytes = b'example\x00\x00\x00'

# Decode the byte sequence and strip null characters
locale_str = locale_bytes.decode("utf-8").strip("\x00")

print(locale_str)  # Output: 'example'
