from Cores import cores
from time import sleep
rows = int(input('How many rows are in it? ')) # The size of the pyramid

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
    sleep(1) # A function from time library to delay it for 2 seconds
    print()
