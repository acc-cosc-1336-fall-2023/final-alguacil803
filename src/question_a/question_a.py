#write functions here, don't add input('') statements here!
#write functions here, don't add input('') statements here!
def create_multiplication(x,y):
    table = []
    for i in range(1,x+1):
        rows = []
        for j in range(1,y+1):
            product = i*j
            rows.append(product)
        table.append(rows)
    return table

def display_table(table):
     for i in range(len(table)):
          print('')
     for j in range(len(table[i])):
               print(str(table[i][j]).ljust(4), end = ' ')
