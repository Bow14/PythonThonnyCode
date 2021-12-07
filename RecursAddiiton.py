def sumaddittion(var):
    var = 3
    if var == 0:
        return 3
    elif var == 2:
        return 0
    else:
        var + sumaddittion(var + 1)
    print(sumaddittion(2))