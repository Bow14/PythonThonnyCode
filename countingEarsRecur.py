def counting_ears(bunny):
    if bunny == 0:
        return 0
    else:
        return 4 + counting_ears(bunny - 2)
print(counting_ears(4))
    