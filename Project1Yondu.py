def main():
    
    
    '''
    Program starts here.

    '''

    try:    
        reavers = int(input("Enter Reavers Total: "))
        units = int(input('enter units number: '))
        yondu = 1
        quill = 1

    except ValueError:
        print("Enter postive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    #my code starts here:

    celebration = (reavers * 3)
    celebration = (celebration - 6)
    units = (units - celebration)
   
    
    yondu_bank = int(units * 0.13)
    remainingunits = (units - yondu_bank)
    
    
    quill_portion = int(remainingunits * 0.11)
    
    
    aftersplit = (remainingunits - quill_portion)

    
    rbf = (aftersplit % reavers)
    
    final_unit = (aftersplit - rbf)
    crew = int(final_unit / reavers)
    
    
    yondu_bank = crew + yondu_bank
    print("Yondus Share: ", yondu_bank)
    
    quill_portion = crew + quill_portion
    print("Quill Share: ", quill_portion)
    
    print("Crew Share: ", crew)
    print("RBF: ", rbf)
    
    
    #my code ends here!
if __name__ == "__main__":
    main()