
def backwards_string():
    if len(word) == 1:
        return word[0]
    else:
        return word[-1] + backwards_string(word[:-1])