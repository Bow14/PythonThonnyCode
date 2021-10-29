import csv
import sys

class book_line():
    def author_books(self,txt, ln):
        self.txt = txt
        self.ln = ln
book_ALG = []
#book_WOO = []
#book_TTL = []

def author_sorting(auth_line):
    line_parameters = auth_line.strip().split('|')
    if line_parameters[2] == 'ALG':
        book_ALG.append(book_line(line_parameters[0], line_parameters[1]))
 
           
    
fp = open('book_data.txt', encoding="utf8")
contents = fp.readlines()

for line in contents:
    author_sorting(line)
    
for book_line in book_ALG:
    print(len(book_line(fp)))

fp.close()
    