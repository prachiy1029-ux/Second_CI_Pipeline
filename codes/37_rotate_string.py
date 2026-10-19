
def rotate_string(text, positions):
    if not text:
        return text

    positions = positions % len(text)
    return text[positions:] + text[:positions]
