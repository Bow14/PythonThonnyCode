in_file = open("menu.txt" , "r")
out_file = open("sampled.txt", "w")

cash = 20
quantity = 20

for truffle in in_file:
    
    truffle = truffle.rstrip().split(',')
    
    if cash >= float(truffle[2]):
        
        cash -= float(truffle[2])
        
        out_file.write(truffle[0])
        
        quantity += 1
        
in_file.close()
out_file.close()