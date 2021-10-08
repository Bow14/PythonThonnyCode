def cumsum(t):
    lyst = 0 
    empt = []
    for elem in t:
      lyst += elem
      empt.append(lyst)
    return empt
    

def main():
 t = [1, 2, 3]
 print (cumsum(t))


if __name__ == '__main__':
    main()