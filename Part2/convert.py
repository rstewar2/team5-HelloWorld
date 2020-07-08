import csv
import numpy as np
import re

SEP = ','
NODES = dict()
#BETA = 0.85

def read_web_file():
    with open('web-Google.txt', 'r') as input_file:
        for row in input_file:
            if row[0] == '#': continue
            nodes = row.strip().split()
            source = int(nodes[0])
            dest = int(nodes[1])

            if source not in NODES.keys(): NODES[source] = [dest]
            else: NODES[source].append(dest)

def get_total_count():
    return len(NODES)

"""
def create_M():
    M = np.zeros((get_total_count(), get_total_count()))
    for key, val in NODES.items():
        total_connections = len(val)
        for v in val:
            M[key-1, v-1] = 1.0/total_connections
    return M
"""

def create_v0():
    v_initial = np.ones((get_total_count(), 1))
    return np.dot(1.0/get_total_count(), v_initial)

"""
def iterate_V(matrix, vector):
    e = np.ones(get_total_count(),1)
    part1 = np.dot(BETA, np.dot(matrix,vector))
    part2 = np.dot((1 - BETA), np.dot(1.0/get_total_count))
    return np.add(part1, part2)
"""

def write_M_to_file():
    with open('Google_M.csv', 'w') as output:
        for key, val in NODES.items():
            for v in val:
                output.write('{0}{1}{2}{3}{4}\n'.format(key, SEP, v, SEP, 1.0/len(val)))

def write_V_to_file(vector):
    with open('initial_V.txt', 'w') as output:
        for i in range(get_total_count()):
            output.write('{0}{1}{2}\n'.format(i, SEP, vector[i][0]))

read_web_file()
#MAT = create_M()
V_0 = create_v0()
#iterate_V(MAT, V_0)
write_M_to_file()
write_V_to_file(V_0)
