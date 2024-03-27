"""
scanRBP

Scanning and plotting RNA-protein binding from PWM and CLIP data.

Github: https://github.com/grexor/scanRBP
"""

import os
import json
import scanRBP.config
import scanRBP.pwm
import scanRBP.database
import pandas
import math

scanRBP_path = os.path.abspath(__file__)
scanRBP_folder = os.path.dirname(scanRBP_path)
version = open(os.path.join(scanRBP_folder, "version"), "rt").readlines()[0].replace("\n", "").replace("\r", "")

# initialize path module
scanRBP.config.init()
scanRBP.database.init()
scanRBP.pwm.init()

def scan(seq):
    heatmap_data = []
    heatmap_columns = []
    sum_all = 0
    for scan_id, pssm in scanRBP.pwm.pssm.items():
        scores = pssm.calculate(seq)
        scores = [x if x!=-math.inf else 0 for x in scores]
        scores = [x if x>=0 else 0 for x in scores]
        if len(scores)<len(seq):
            scores = scores + [0] * (len(seq)-len(scores))
        sum_all += sum(scores)
        heatmap_data.append(scores)
        heatmap_columns.append(scan_id)
    heatmap_rows = list(seq)
    data = pandas.DataFrame(heatmap_data, index=heatmap_columns, columns=heatmap_rows)
    return data