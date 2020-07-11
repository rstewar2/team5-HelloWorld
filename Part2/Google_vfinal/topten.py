import pandas as pd

NODES = {}
SEP = ','

with open('part-00000', 'r') as input_file:
    for row in input_file:
        elements = row.strip().split(SEP)
        #print (elements)
        node = int(elements[0])
        prob = float(elements[1])
        NODES[node] = prob

df = pd.DataFrame.from_dict(NODES, orient='index', columns=['Prob'])

topten = df.nlargest(10, 'Prob')

print (topten)