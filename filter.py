#!/usr/bin/env python
import numpy as np

from sys import argv
import os
import matplotlib.pyplot as plt



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
    contig_set = {}

    x = []
    y = []

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
                        contig_set[contig] = contig_count

    with open('{}/out.windowed.pi'.format(fold)) as input_handle:
        for num, line in enumerate(input_handle):
            if num != 0:
                split_line = line.split("\t")
                probability = split_line[-2].strip()
                contig = split_line[0]
                contig_count = contig_set[contig]
                x.append(contig_count)
                y.append(float(probability))

    plt.figure(figsize=(21,3))
    #plt.axis('tight')
    plt.scatter(x, np.log10(y), s=1, c=color, marker='o', cmap=None, norm=None, vmin=None,
            vmax=None, alpha=None, linewidths=0, verts=None, edgecolors=color,
            hold=None, data=None)
    plt.ylim([0, 3])
    plt.savefig("{}_sliding_window_pi.eps".format(fold), format="eps")
    #plt.show()
    #exit()
