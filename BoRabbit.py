def do_research(cages, adults, babies):
    with open('rabbits.csv', "w") as rabbit:
        month = 1
        total = 1
        rabbit.write("# Table of rabbit pairs")
        rabbit.write("Month, Adult, Babies, Total")
        while total < cages:
            rabbit.write(f"{month}, {adults}, {babies}, {total}\n")
            new_adult = adults + babies
            new_babies = adults - babies
            total = new_adult + new_babies
        rabbit.write(f"{month}, {new_adult}, {new_babies}, {total}\n")
        rabbit.write(f"# Cages will ruin out in month {month}")
do_research(500, 1, 0)
    