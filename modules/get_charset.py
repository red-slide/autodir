async def get_charset():
    charset = input("\033[36m[+]\033[0m Enter the charset: ").replace(' ', '')

    unique_chars = []
    seen = set()

    for char in charset:
        if char not in seen:
            unique_chars.append(char)
            seen.add(char)

    charset_no_duplicates = ''.join(unique_chars)

    return charset_no_duplicates
