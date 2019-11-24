def is_isbn_or_key(string):
    isbn_or_key = 'key'
    if len(string) == 13 and string.isdigit():
        isbn_or_key = 'isbn'
    short_str = string.replace('-', '')
    if len(short_str) == 10 and '-' in short_str and short_str.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
