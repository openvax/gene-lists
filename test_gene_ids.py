#!/usr/bin/env python3

import pandas as pd
from glob import glob
from pyensembl import ensembl_grch38

for csv_file in glob("*.csv"):
    print("-- %s:" % csv_file)
    df = pd.read_csv(csv_file)
    gene_ids = df["Ensembl Gene ID"]
    names = df["Gene"]
    for name, gene_id in zip(names, gene_ids):
        gene = ensembl_grch38.gene_by_id(gene_id)
        print(name, gene_id, gene)
        if gene.name != name:
            print("Warning: %s != %s" % (name, gene.name))
