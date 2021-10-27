import csv

legends_csv = "Users/huffn/Desktop/ThonnyCode_folder/legends_data.csv"

def fetch_legends_data(legends_csv):
    """Return movie data from a CSV file"""
    with open(legends_csv, "r") as legends_file:
        reader = csv.reader(legends_file)
        legends_info = []
        for column in textform:
          legends_info.append(column)
        return legends_info

def print_legends_data(data):
    """Print the legend data in easy to read columns"""
    for legends, mastery, date, skinsowned in data:
      print("{:36} {:10} {:18} ${:16} {}".format(legends, mastery, date, skinsowned))
      
def sort_legends_data(data, index):
    "Sorting"
    header = data[0]
    sorted_legends = data[1:]
    sorted_legends.sort(key=operator.itemgetter(index))
    sorted_legends.insert(0, header)
    return sorted_legends


legends_data = fetch_legends_data(legends_csv) 
print_legends_data(legends_data)