from Cores import cores
from time import sleep

def readInt(msg):
    ok = False
    value = 0
    while True:
        rows = str(input(msg))
        if rows.isnumeric():
            value = int(rows)
            ok = True
        else:
            print('{}ERROR! Type an integer valid number.{}'.format(cores['amarelo'], cores['limpa']))
        if ok:
            break
    return value

rows = readInt('How many rows are in it? ') # The size of the pyramid

if rows > 100: # Time to conclude the task
    print('{}Please, sit! It will take more time than Windows Updating!{}'.format(cores['azul'], cores['limpa']))


print('{}PROCESSING...\n{}'.format(cores['pretoebranco'], cores['limpa']))
sleep(2) # A function from time library to delay it for 2 seconds

for i in range(1, rows + 1): # To set the range
    for j in range(rows-i): # First underscore
        print("{}_{}".format(cores['amarelo'], cores['limpa']), end = "")
    for k in range(1, i): # First asterisks
        print("{}*{}".format(cores['pretoebranco'], cores['limpa']), end = "")
    for l in range(i, 0, -1): # Asterisks from midle
        print("{}*{}".format(cores['pretoebranco'], cores['limpa']), end = "")
    for m in range(rows-i): # Last underscore
        print("{}_{}".format(cores['amarelo'], cores['limpa']), end = "")
    sleep(1) # A function from time library to delay each row for 1 second
    print()
