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
import pandas as pd
import numpy as np
import math

scanRBP_path = os.path.abspath(__file__)
scanRBP_folder = os.path.dirname(scanRBP_path)
version = open(os.path.join(scanRBP_folder, "version"), "rt").readlines()[0].replace("\n", "").replace("\r", "")

# initialize path module
scanRBP.config.init()
scanRBP.database.init()
scanRBP.pwm.init()

def scan(seq):
    heatmap_columns = []
    heatmap_data = []
    
    seq_len = len(seq)
    
    for scan_id, pssm in scanRBP.pwm.pssm.items():
        scores = np.array(pssm.calculate(seq), dtype=np.float32)
        
        # replace -inf with 0 and remove negatives in one operation
        scores = np.where(scores == -math.inf, 0, scores)
        scores = np.maximum(scores, 0)

        # ensure scores array matches sequence length
        if scores.shape[0] < seq_len:
            scores = np.pad(scores, (0, seq_len - scores.shape[0]), constant_values=0)

        heatmap_data.append(scores)
        heatmap_columns.append(scan_id)

    return pd.DataFrame(heatmap_data, index=heatmap_columns, columns=list(seq))
