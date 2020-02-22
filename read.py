inp = open('input.txt', 'r')
# i need take vars in the txt file
def tx():
    for line in inp:    
        print(line)
        print(line[0])
        
tx()