def inverse_dict(b):
 
    inverse = {}
    for dic in b:
        Value = b[dic]
        inverse.setdefault(Value, []).append(dic)
    return inverse


if __name__ == '__main__':
    b = dict(a=1, b=2, c=3, z=1)
    inverse = inverse_dict(b)
    for Value in inverse:
        dic = inverse[Value]
    print(inverse)