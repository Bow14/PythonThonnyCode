def main():

    with open('book_data.txt', 'r') as main_file:
        data = list(csv.reader(main_file, delimiter='|'))
        book_info = {}
        for line in data:
            text, page_number, code = line
            page_number = int(page_number)
            if code in book_info:
                val = book_info[code]
                val.append((page_number, text))
            else:
                book_info[code] = []
                #book_info[code].append