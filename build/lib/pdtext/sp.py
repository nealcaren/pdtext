def extract_pos(doc, pos, return_list = True):
    tokens = [t.text for t in doc if t.pos_ == pos]
    if return_list == False:
        return ', '.join(tokens)

    return tokens
