

def do_research():
    cages = 500
    adult_rabbits = 1
    baby_rabbits = 0
    month = 1
    total = 1
    adult = adult_rabbits
    babies = baby_rabbits
    while total < cages:  
        month = month + 1
        new_adults = baby_rabbits + adult_rabbits
        new_babies = adult_rabbits
        adults = new_adults
        babies = new_babies
        total = adults + babies
        
        print(month, new_adults, new_babies, total)
do_research()
    