import os
import sys
import gzip
import glob

print("reading in gene info")
genes = {}
f = gzip.open("ncbi_gene_info.tab.gz", "rt")
header = f.readline().replace("\r", "").replace("\n", "").split("\t")
r = f.readline()
while r:
    r = r.replace("\r", "").replace("\n", "").split("\t")
    data = dict(zip(header, r))
    symbol = data["Symbol"]
    genes[symbol] = data
    aliases = data["Aliases"].split(", ")
    for alias in aliases:
        genes[alias] = data
    r = f.readline()
f.close()

print("constructing RBP database")
fout = gzip.open("scanRBP.tab.gz", "wt")
header = ["scan_id", "protein", "tissue", "cluster", "pwm_path", "aliases", "description", "name_search"]
fout.write("\t".join(header) + "\n")
files = glob.glob("pwm/*.mat")
for fname in files:
    temp = os.path.basename(fname)
    tissue = temp.split(".")[0]
    protein = temp.split(".")[1]
    cluster = temp.split(".")[-2]
    gene_data = genes[protein]
    aliases = ",".join(gene_data["Aliases"].split(", "))
    name_search = aliases.replace("-", "")
    desc = gene_data["description"]
    pwm_path = "pwm/"+temp
    scan_id = f"{protein}.{tissue}.{cluster}"
    row = [scan_id, protein, tissue, cluster, pwm_path, aliases, desc, name_search]
    fout.write("\t".join(row) + "\n")
fout.close()