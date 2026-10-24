# UTF-8 Validation

Determines whether a list of integers (each one byte) is a valid UTF-8 encoding.

## Rules
- 1 byte:  0xxxxxxx
- 2 bytes: 110xxxxx 10xxxxxx
- 3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
- 4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Only the 8 least significant bits of each integer are used.

## File
- `0-validate_utf8.py`: `validUTF8(data)` returns True or False.
