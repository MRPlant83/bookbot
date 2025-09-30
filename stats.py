def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            chars[lowered] = chars.get(lowered, 0) + 1
    return chars


def sort_dict_by_value(d, reverse=True):
    items = list(d.items())
    items.sort(key=lambda x: x[1], reverse=reverse)
    return dict(items)
