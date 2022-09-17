def two_characters(text: str) -> int:

    char_set = list(set(text))
    if len(char_set) < 2:
        return 0
    
    max_alt_len = 0
    for char_1 in char_set:
        for char_2 in char_set:
            if char_2 == char_1:
                continue

            texts = [ch for ch in text if ch == char_1 or ch == char_2]
            is_valid = True
            for i in range(len(texts) - 1):
                if texts[i] == texts[i+1]:
                    is_valid = False
                    break
            if is_valid and max_alt_len < len(texts):
                max_alt_len = len(texts)

    return max_alt_len
