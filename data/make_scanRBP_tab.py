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
header = ["scan_id", "protein", "tissue", "source", "cluster", "pwm_path", "aliases", "description", "name_search"]
fout.write("\t".join(header) + "\n")

# mcross
files = glob.glob("mcross/*.mat")
for fname in files:
    temp = os.path.basename(fname)
    tissue = temp.split(".")[0]
    protein = temp.split(".")[1]
    cluster = temp.split(".")[-2]
    gene_data = genes[protein]
    aliases = ",".join(gene_data["Aliases"].split(", "))
    name_search = aliases.replace("-", "")
    desc = gene_data["description"]
    pwm_path = "mcross/"+temp
    scan_id = f"{protein}.{tissue}.{cluster}"
    row = [scan_id, protein, tissue, "mCross", cluster, pwm_path, aliases, desc, name_search]
    fout.write("\t".join(row) + "\n")

# cisbp
f = open("cisbp/RBP_Information.txt", "rt")
header = f.readline().replace("\r", "").replace("\n", "").split("\t")
r = f.readline()
while r:
    r = r.replace("\r", "").replace("\n", "").split("\t")
    data = dict(zip(header, r))
    motif_id = data["Motif_ID"]
    if motif_id!=".":
        rbp_name = data["RBP_Name"].upper()
        if os.path.exists(f"cisbp/pfm/{motif_id}.txt"):
            gene_data = genes.get(rbp_name, {"description":"", "Aliases":rbp_name})
            desc = gene_data["description"]
            aliases = ",".join(gene_data["Aliases"].split(", "))
            name_search = aliases.replace("-", "")
            row = [f"{rbp_name}.{motif_id}", rbp_name, "", "cisbp-rna", "", f"cisbp/pfm/{motif_id}.txt", aliases, desc, name_search]
            fout.write("\t".join(row) + "\n")
    r = f.readline()
f.close()

fout.close()