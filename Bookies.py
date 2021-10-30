


def summary_function(list):
    longest = ''
    longest_index = 0
    shortest = ''
    shortest_index = 0
    qty = 0
    total = 0
    
    for index, sentence in enumerate(list):
        if index == 0:
            longest = sentence[2]
            shortest = sentence[2]
            longest_index = index
            shortest_index = index
            qty =0
            total = 0
        else:
            if len(sentence[2]) > len(longest):
                longest = sentence[2]
                longest_index = index
            elif len(sentence[2]) < len(shortest):
                shortest = sentence[2]
                shortest_index = index
        total += sentece[1]
        qty += 1
        
        
    average = total/qty
    
    return longest, shortest, longest_index, shortest_index, average

def main():
    
    with open('book_data.txt', 'r', encoding='utf-8') as fp:

        book_initial_1 = ''
        book_initial_2 = ''
        book_initial_3 = ''

        fp = fp.readlines()
        
        book_data = []

        for line in fp:
            fp = line.strip('\n').split('|')
            fp = [fp[0], int(fp[1]), fp[2]] #formating
            book_data.append(fp)
            

        book_inital_1 = book_data[0][2]
        remaining_initals = []
        
        for line in book_data:
            if line[2] != book_inital_1:
                remaining_initals.append(line[2]) #Goes through list of info and check book_initals if its woo then keep it
                
        book_inital_2 = remaining_initals[1]
        for line in remaining_initals
            if line != book_inital_2:
                book_inital_3 = line 
        
        book_ALG =[]
        book_Woo = []
        book_TTL = [] 
        
        for line in book_data:
            if book_inital_1 in line:
                book_Woo.append(line)
            elif book_inital_2 in line:
                book_TTL.append(line)
            elif book_inital_3 in line:
                book_ALG.append(line)
    
    
    
    
    
    

    
if __name__ == '__main__':
    main()




 