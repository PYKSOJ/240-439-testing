def alternating_char(text: str) -> int:
    remove_counter = 0
    index = 0
    tmp_text = text[:]
    while index < len(tmp_text)-1:
        if tmp_text[index] == tmp_text[index+1]:
            tmp_text = tmp_text[:index] + tmp_text[index+1:]
            remove_counter += 1
        else:
            index += 1
    return remove_counter
