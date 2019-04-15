import numpy as np
import os

BASE_DIR = "/home/turja"
NETWORK_DIR = os.path.join(BASE_DIR, "AD_network")
STAT_DIR = os.path.join(BASE_DIR, "AD_stats")


def read_matrix_from_text_file(subject, debug=False):
    file_path = os.path.join(NETWORK_DIR, subject + "_fdt_network_matrix")
    if debug:
        print("Reading File: " + file_path)
    a = []
    fin = open(file_path, 'r')
    for line in fin.readlines():
        a.append([float(x) for x in line.split()])

    a = np.asarray(a)
    return a
