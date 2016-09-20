#!/usr/bin/env python
import numpy as np
from Bio import SeqIO
from sys import argv
import os
import matplotlib.pyplot as plt
import pickle

assembly_path = ""

if len(argv) > 1:
    folders = argv[1:]
else:
    folders = [i for i in os.listdir(os.getcwd()) if os.path.isdir(i)]

for fold in folders:
    if not os.path.isdir(fold):
        continue
    fold = os.path.basename(fold)
    if fold =='rano':
        color = "#ffc44f"
    elif fold =='toro':
        color = '#C000FF'
    elif fold == 'kian8.1':
        color = '#0080FF'
    elif fold == 'kian8.4':
        color = '#FF0000'
    elif fold == 'kar3':
        color = '#00C000'
    else:
        color = None

    print(color, fold)
    plt.title(fold)

    contig_count = 0
    contig_set = set()

    x = []
    y = []
    if not os.path.isfile('fave_pickle.p'):
        all_folders = [i for i in os.listdir(os.getcwd()) if os.path.isdir(i)]
        for fold2 in all_folders:
            with open('{}/out.windowed.pi'.format(fold2)) as input_handle:
                for num, line in enumerate(input_handle):
                    if num != 0:
                        split_line = line.split("\t")
                        probability = split_line[-2].strip()
                        contig = split_line[0]
                        if contig not in contig_set:
                            contig_count += 1
                            contig_set.add(contig)

        new_contig_set = {}
        num = 0
        with open(assembly_path) as input_handle:
            for contig in SeqIO.parse(input_handle, 'fasta'):
                if contig.id in contig_set:
                    num += 1
                    new_contig_set[contig.id] = num

        with open('fave_pickle.p', 'w+') as pickle_dump:
            pickle.dump(new_contig_set, pickle_dump)

    with open('fave_pickle.p') as pickle_handle:
        contig_set = pickle.load(pickle_handle)

    with open('{}/out.windowed.pi'.format(fold)) as input_handle:
        for num, line in enumerate(input_handle):
            if num != 0:
                split_line = line.split("\t")
                probability = split_line[-2].strip()
                contig = split_line[0]
                contig_count = contig_set[contig]
                x.append(contig_count)
                y.append(float(probability))
    print(max(x))

    plt.subplot(210+number)
    plt.scatter(x, np.log10(y), s=1, c=color, marker='o', cmap=None, norm=None, vmin=None,
            vmax=None, alpha=None, linewidths=0, verts=None, edgecolors=color,
            hold=None, data=None)
    plt.ylim([0, 3])
    plt.xlim([0, len(contig_set)])
#
#plt.savefig("{}_sliding_window_pi.eps".format(fold), format="eps")
plt.show()
exit()
