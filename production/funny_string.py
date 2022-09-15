def funny_string(text):
    rev_text = text[::-1]
    ascii_diffs = [abs(ord(text[i]) - ord(text[i+1])) for i in range(len(text) - 1)]
    rev_ascii_diffs = [abs(ord(rev_text[i]) - ord(rev_text[i+1])) for i in range(len(rev_text) - 1)]

    if ascii_diffs == rev_ascii_diffs:
        return 'Funny'
    return 'Not Funny'