import csv
from sys import argv 

def summary_function(data_list):
    authors_data = dict()
    
    

    for line in data_list:
        sentence = line[0]
        current_sentence_length = len(sentence)
        sentence_page_num = int(line[1])
        author = line[2]

        if author in authors_data:
            data = authors_data[author]
            longest_line = data[0]
            shortest_line = data[1]

            if current_sentence_length > longest_line:
                data[0] = current_sentence_length
                data[4] = sentence
            elif current_sentence_length == longest_line:
                data[0] = sentence_page_num
                data[4] = sentence

            if current_sentence_length < shortest_line:
                data[0] = current_sentence_length
                data[4] = sentence
            elif current_sentence_length == shortest_line:
                data[1] = sentence_page_num
                data[5] = sentence

            data[2] += current_sentence_length
            data[3] += 1

        else:
            authors_data[author] = [current_sentence_length, current_sentence_length, current_sentence_length, 1, sentence, sentence]



    with open('novel_summary.txt', 'w')as out_file:
        keys = list(authors_data.keys())
        keys.sort()
        for key in keys:
            author = key
            data = authors_data[key]
            longest_line = data[0]
            longest_sentence = data[4]
            shortest_line = data[1]
            shortest_sentence = data[5]
            
            
            total = data[2]
            qty = data[3]
            avg = int(total/qty)
            
            out_file.write(f'{author}\n') 
            out_file.write(f'Longest line ({longest_line}): {longest_sentence}\n')
            out_file.write(f'Shortest line ({shortest_line}): {shortest_sentence}\n')
            out_file.write(f'Average length: {avg}\n\n')
        
       

    
def sort_text(text):
    return text[1]

def creat_novel_text(data_list):
    author_texts = dict()
   
    for line in data_list:
        sentence = line[0]
        sentence_page_num = int(line[1])
        author = line[2]
        
    
        if author in author_texts:
            author_texts[author].append( [sentence, sentence_page_num])

        else:
            author_texts[author] = [[sentence, sentence_page_num]]
    for author in author_texts:
        text = author_texts[author]
        sorted_text = sorted(text, key=sort_text)
        author_texts[author] = sorted_text
        
    with open('novel_text.txt', 'w')as novel_text:
        keys = list(author_texts.keys())
        keys.sort()
        
        for key in keys:
            texts = author_texts[key]
            novel_text.write(f'{key}\n')
            for text in texts:
                novel_text.write(f'{text[0]}\n')
            novel_text.write('-----\n')


def main():

    with open('book_data.txt', 'r') as fp:
        data = list(csv.reader(fp, delimiter='|'))
        creat_novel_text(data)
        author_data = summary_function(data)
        


    
if __name__ == '__main__':
    main()
