import scanRBP
import gzip
import os
import sys

proteins = {}

def init():
    database_file = f"{scanRBP.config.data_folder}/scanRBP.tab.gz"
    if not os.path.exists(database_file):
        if not os.path.exists(scanRBP.config.data_folder):
            os.makedirs(scanRBP.config.data_folder)
        os.system(f"wget https://github.com/grexor/scanRBP/raw/main/data/data.tar.gz -O {scanRBP.config.data_folder}/data.tar.gz >/dev/null 2>&1")
        os.system(f"tar xfz {scanRBP.config.data_folder}/data.tar.gz -C {scanRBP.config.data_folder}")
    f = gzip.open(database_file, "rt")
    header = f.readline().replace("\r", "").replace("\n", "").split("\t")
    r = f.readline()
    while r:
        r = r.replace("\r", "").replace("\n", "").split("\t")
        data = dict(zip(header, r))
        proteins[data["scan_id"]] = data
        r = f.readline()
    f.close()
